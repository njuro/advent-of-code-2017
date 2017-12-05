'''
https://adventofcode.com/2017/day/5
'''


def instruction_maze(part2=False):
    with open("input.txt", 'r') as input:
        instructions = list(map(int, input.readlines()))
    index, steps = 0, 0
    while True:
        try:
            shift = -1 if instructions[index] > 2 and part2 else 1
            instructions[index] += shift
        except IndexError:
            return steps
        index += instructions[index] - shift
        steps += 1


# Part 1
print(instruction_maze())
# Part 2
print(instruction_maze(part2=True))
