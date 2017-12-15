'''
https://adventofcode.com/2017/day/15
'''


def dueling_generators(modulo=False):
    a = generate_value(512, 16807, 4, modulo)
    b = generate_value(191, 48271, 8, modulo)
    count = 0
    times = 5000000 if modulo else 40000000

    for _ in range(times):
        x, y = next(a), next(b)
        count += 1 if bin(x)[-16:] == bin(y)[-16:] else 0

    return count


def generate_value(default_value, factor, modulo, use_modulo):
    n = default_value
    while True:
        n = (n * factor) % 2147483647
        if use_modulo and n % modulo != 0:
            continue
        yield n


# Part 1
print(dueling_generators())
# Part 2
print(dueling_generators(modulo=True))
