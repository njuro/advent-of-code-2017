'''
https://adventofcode.com/2017/day/21
'''

import numpy as np


def fractals(full=False):
    grid = np.asarray([[".", "#", "."], [".", ".", "#"], ["#", "#", "#"]])

    def convert_from(inp):
        return [list(s) for s in inp.strip().split("/")]

    def convert_to(grid):
        return "/".join(["".join(row) for row in grid])

    def permutations(key):
        perms = []
        for i in range(0, 4):
            rotated = np.rot90(key, k=i)
            perms.append(rotated)
            perms.append(np.flipud(rotated))
            perms.append(np.fliplr(rotated))
        return list(map(convert_to, perms))

    rules = {l.strip(): convert_from(r)
             for l, r in [line.split("=>") for line in open("input.txt").readlines()]}

    new_rules = {}
    for key, value in rules.items():
        new_rules.update({new_key: value for new_key in permutations(convert_from(key))})
    rules.update(new_rules)

    def split(grid, n):
        blocks = []
        columns = np.hsplit(grid, n)
        for i in range(n):
            blocks.extend(np.vsplit(columns[i], n))
        return blocks

    def merge(blocks, n):
        return np.hstack([np.vstack(chunk) for chunk in np.split(blocks, n)])

    for i in range(18 if full else 5):
        n = len(grid) // (2 if len(grid) % 2 == 0 else 3)
        transformed = [rules[convert_to(block)] for block in split(grid, n)]
        grid = merge(np.asarray(transformed), n)

    return sum([row.count("#") for row in grid.tolist()])


# Part 1
print(fractals())
# Part 2
print(fractals(full=True))
