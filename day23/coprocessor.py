'''
https://adventofcode.com/2017/day/23
'''

from collections import defaultdict

instructions = [line.strip() for line in open("input.txt")]


def processor1():
    global instructions

    def get_val(n):
        return registers[n] if n.isalpha() else int(n)

    registers = defaultdict(int)
    count, position = 0, 0

    while 0 <= position < len(instructions) - 1:
        cmd, x, y = instructions[position].split(" ")
        y = get_val(y)

        if cmd == "set":
            registers[x] = y
        elif cmd == "sub":
            registers[x] -= y
        elif cmd == "mul":
            registers[x] *= y
            count += 1
        elif cmd == "jnz":
            if get_val(x) != 0:
                position += y
                continue

        position += 1

    return count


def processor2():
    iterations, count = 0, 0
    start = 65 * 100 + 100000

    while iterations <= 1000:
        for i in range(2, start):
            if start % i == 0:
                count += 1
                break
        start += 17
        iterations += 1
    return count


# Part 1
print(processor1())

# Part 2
print(processor2())
