'''
https://adventofcode.com/2017/day/22
'''

from math import floor


def virus():
    inp = open("input.txt").read().splitlines()
    x = y = floor(len(inp) // 2)
    grid = {(i, j): ('I' if inp[i][j] == '#' else 'C') for i in range(len(inp)) for j in range(len(inp))}

    directions = ['U', 'R', 'D', 'L']
    status = ['C', 'W', 'I', 'F']
    index = infected = 0

    for _ in range(10000000):
        if (x, y) not in grid.keys():
            grid[(x, y)] = 'C'

        cell = grid[(x, y)]
        if cell == 'C':
            index -= 1
        elif cell == 'W':
            infected += 1
        elif cell == 'I':
            index += 1
        elif cell == 'F':
            index += 2

        grid[(x, y)] = status[(status.index(cell) + 1) % len(status)]
        index %= len(directions)
        direction = directions[index]

        if direction == 'R':
            y += 1
        elif direction == 'U':
            x -= 1
        elif direction == 'L':
            y -= 1
        else:
            x += 1

    return infected


# Part 2
print(virus())
