'''
https://adventofcode.com/2017/day/11
'''


def hex_grid():
    instructions = open("input.txt", 'r').read().split(",")
    shifts = {
        "n": (1, -1, 0),
        "s": (-1, 1, 0),
        "ne": (0, -1, 1),
        "sw": (0, 1, -1),
        "nw": (1, 0, -1),
        "se": (-1, 0, 1)
    }
    x, y, z, distance, max_distance = 0, 0, 0, 0, 0

    for inst in instructions:
        shift = shifts[inst]
        x += shift[0]
        y += shift[1]
        z += shift[2]
        distance = (abs(x) + abs(y) + abs(z)) // 2
        max_distance = max(distance, max_distance)

    return distance, max_distance


dist, max_dist = hex_grid()
# Part 1
print(dist)
# Part 2
print(max_dist)
