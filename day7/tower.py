'''
https://adventofcode.com/2017/day/7
'''

import re
from collections import defaultdict


class Program:

    def __init__(self, name, weight, children):
        self.name = name
        self.weight = int(weight)
        # Weight of this program + weight of all his children
        self.total_weight = self.weight
        self.parent = None
        self.children = children
        # What should be each children weight for tower to be balanced
        self.correct_child_weight = 0

    def __str__(self):
        return ", ".join([self.name, str(self.weight)])


def tower(unbalanced=False):
    regexp = re.compile(r'(\w+) \((\d+)\)')
    programs = []
    all_children = ()
    with open("input.txt", 'r') as input:
        for line in input:
            # Parse name and weight
            name, weight = regexp.match(line).groups()
            # Parse children, if present
            children = line.split("->")[1].strip().split(", ") if "->" in line else []
            programs.append(Program(name, weight, children))
            # Append children to the list of all children (without duplicates)
            all_children += tuple(children)

    # find root - the only program which does not appear as child anywhere
    root = next(iter([program for program in programs if program.name not in all_children]))
    if not unbalanced:
        # Part 1 ends here
        return root.name

    tower = create_tower(root, programs)
    calculate_weight(tower)
    return find_unbalanced(tower)


def create_tower(root, programs):
    '''
    Creates tree-like structure by replacing program names in children with actual Program objects and also sets parent object

    :param root of the tower
    :param programs list
    :return root
    '''
    # Convert program names to programs
    root.children = list(filter(lambda program: program.name in root.children, programs))
    for child in root.children:
        child.parent = root
        # Process all children recursively
        create_tower(child, programs)
    return root


def calculate_weight(root):
    '''
    Calculates total weight of every program by adding its weight and weight of his children

    :param root of the tower
    :return total weight of the root
    '''
    root.total_weight += sum([calculate_weight(child) for child in root.children])
    return root.total_weight


def find_unbalanced(root):
    '''
    Finds unbalanced program
    :param root
    :return: unbalanced program
    '''
    # group children by their total weights
    weights = defaultdict(list)
    for child in root.children:
        weights[child.total_weight].append(child)
        if len(weights[child.total_weight]) > 1:
            # more than one children have this weight, so it must be the correct weight for this tower
            root.correct_child_weight = child.total_weight

    if len(weights.keys()) == 1:
        # all children have the same weight, so this program must be unbalanced
        return root

    for childs in weights.values():
        if len(childs) == 1:
            # only one children has this weight, therefore the unbalanced program is somewhere in this subtree
            return find_unbalanced(childs[0])


# Part 1
print("Root of tower:", tower())
# Part 2
unbalanced = tower(unbalanced=True)
print(unbalanced.name, "- Actual weight:", unbalanced.total_weight, "Expected weight:",
      unbalanced.parent.correct_child_weight)
