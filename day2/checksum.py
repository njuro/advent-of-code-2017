'''
https://adventofcode.com/2017/day/2
'''


def checksum(evenly=False):
    with open("input.txt", 'r') as input:
        checksum = 0
        for line in input.readlines():
            row = list(map(int, line.split()))
            if evenly:
                checksum += next((x // y for x in row for y in row if x != y and x % y == 0), 0)
            else:
                checksum += max(row) - min(row)
        return checksum


# Part 1
print(checksum())
# Part 2
print(checksum(evenly=True))
