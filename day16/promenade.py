'''
https://adventofcode.com/2017/day/16
'''


def promenade(full_dance=False):
    programs = list(map(chr, range(ord('a'), ord('p') + 1)))
    copy = programs[:]
    moves = open("input.txt").read().split(",")

    # Calculate the length of cycle
    cycle = 0
    while full_dance:
        cycle += 1
        copy = perform_dance(copy, moves)
        if copy == programs:
            break

    iterations = 10 ** 9 % cycle if full_dance else 1
    for _ in range(iterations):
        programs = perform_dance(programs, moves)

    return "".join(programs)


def perform_dance(programs, moves):
    for move in moves:
        if move.startswith("s"):
            size = int(move[1:])
            programs = programs[-size:] + programs[:-size]
        elif move.startswith("x"):
            x, y = move[1:].split("/")
            programs[int(x)], programs[int(y)] = programs[int(y)], programs[int(x)]
        elif move.startswith("p"):
            x, y = move[1:].split("/")
            ix, iy = programs.index(x), programs.index(y)
            programs[ix], programs[iy] = programs[iy], programs[ix]

    return programs


# Part 1
print(promenade())
# Part 2
print(promenade(full_dance=True))
