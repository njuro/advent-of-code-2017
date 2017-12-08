'''
https://adventofcode.com/2017/day/8
'''

import re
from collections import defaultdict


def instructions(get_max=False):
    regexp = re.compile(r'(\w+) (\w{3}) ([-]?\d+) if (\w+) (.+)')
    registers = defaultdict(lambda: 0)
    max_val = -10 ** 10

    with open("input.txt", 'r') as input:
        for line in input:
            reg, op, val, c_reg, cond = regexp.match(line).groups()
            cond = str(registers[c_reg]) + cond.strip()
            val = int(val)
            max_val = max(max(registers.values(), default=max_val), max_val)
            if eval(cond):
                if op == "inc":
                    registers[reg] += val
                else:
                    registers[reg] -= val

    return max_val if get_max else max(registers.values())


# Part 1
print(instructions())
# Part 2
print(instructions(get_max=True))
