'''
https://adventofcode.com/2017/day/18
'''

import multiprocessing.pool
from collections import defaultdict
from multiprocessing import Queue

instructions = [line.strip() for line in open("input.txt")]


def duet(id=0, inpq=None, outq=None):
    global instructions

    def get_val(n):
        return registers[n] if n.isalpha() else int(n)

    registers = defaultdict(int)
    registers['p'] = id
    played, count, position = None, 0, 0

    while 0 <= position < len(instructions) - 1:
        cmd, args = instructions[position].split(" ", maxsplit=1)
        args = args.split(" ")
        if cmd == "set":
            registers[args[0]] = get_val(args[1])
        elif cmd == "add":
            registers[args[0]] += get_val(args[1])
        elif cmd == "mul":
            registers[args[0]] *= get_val(args[1])
        elif cmd == "mod":
            n = get_val(args[1])
            if n != 0:
                registers[args[0]] %= n
        elif cmd == "jgz":
            if get_val(args[0]) > 0:
                position += get_val(args[1])
                continue
        elif cmd == "snd":
            if outq:
                outq.put(get_val(args[0]))
                count += 1
            else:
                played = get_val(args[0])
        elif cmd == "rcv":
            if inpq:
                registers[args[0]] = inpq.get()
            elif get_val(args[0]) != 0:
                return played

        position += 1
    return count


# Part 1
print(duet())

# Part 2
valuesA, valuesB = Queue(), Queue()
pool = multiprocessing.pool.ThreadPool(processes=2)
res1 = pool.apply_async(duet, (0, valuesA, valuesB))
res2 = pool.apply_async(duet, (1, valuesB, valuesA))
print(res2.get())
