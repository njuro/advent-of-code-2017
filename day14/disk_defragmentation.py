'''
https://adventofcode.com/2017/day/14
'''

from day10.knot_hash import knot_hash


def disk_defragmentation(input):
    size, count, reg_count = 128, 0, 0
    regions, grid = [], []

    for i in range(size):
        hash = "".join([bin(int(c, 16))[2:].zfill(4) for c in knot_hash(input + "-" + str(i), total=True)])
        count += hash.count('1')
        grid.append(hash)

    for x in range(size):
        for y in range(size):
            if grid[x][y] == '0' or (x, y) in regions:
                continue
            reg_count += 1
            stack = [(x, y)]
            regions.append((x, y))

            while stack:
                u, v = stack.pop(0)
                neighbours = [(u + 1, v), (u - 1, v), (u, v + 1), (u, v - 1)]
                for u, v in neighbours:
                    if u in range(size) and v in range(size) and grid[u][v] == '1' and (u, v) not in regions:
                        stack.append((u, v))
                        regions.append((u, v))

    return count, reg_count


input = "stpzcrnm"
count, reg_count = disk_defragmentation(input)

# Part 1
print(count)
# Part 2
print(reg_count)
