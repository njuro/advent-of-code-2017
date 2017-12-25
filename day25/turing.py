'''
https://adventofcode.com/2017/day/25
'''

from collections import defaultdict


def turing():
    tape = defaultdict(int)
    state, cursor, steps = 'A', 0, 12172063

    states = {
        ('A', 0): (1, 1, 'B'),
        ('A', 1): (0, -1, 'C'),
        ('B', 0): (1, -1, 'A'),
        ('B', 1): (1, -1, 'D'),
        ('C', 0): (1, 1, 'D'),
        ('C', 1): (0, 1, 'C'),
        ('D', 0): (0, -1, 'B'),
        ('D', 1): (0, 1, 'E'),
        ('E', 0): (1, 1, 'C'),
        ('E', 1): (1, -1, 'F'),
        ('F', 0): (1, -1, 'E'),
        ('F', 1): (1, 1, 'A')
    }

    for _ in range(steps):
        tape[cursor], shift, state = states[(state, tape[cursor])]
        cursor += shift

    return list(tape.values()).count(1)


print(turing())
