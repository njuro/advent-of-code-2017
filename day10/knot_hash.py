'''
https://adventofcode.com/2017/day/10
'''


def knot_hash(input_str=None, total=False):
    if input_str:
        # takes input from string
        lengths = list(map(ord, [c for c in input_str])) + [17, 31, 73, 47, 23]
    else:
        with open("input.txt", 'r') as input:
            # takes input from file
            if total:
                lengths = list(map(ord, [c for c in input.read()])) + [17, 31, 73, 47, 23]
            else:
                lengths = list(map(int, input.readline().split(",")))

    size = 256
    values = [i for i in range(size)]
    position, skip = 0, 0
    rounds = 64 if total else 1

    for _ in range(rounds):
        for length in lengths:
            start, end = position, (position + length)
            copy = values[:]
            for i in range(start, end):
                values[i % size] = copy[(start + end - 1 - i) % size]
            position = (position + length + skip) % size
            skip += 1

    if not total:
        # end of part 1
        return values[0] * values[1]

    dense = ""
    for i in range(0, size, 16):
        block = values[i]
        for j in range(i + 1, i + 16):
            block ^= values[j]
        dense += format(block, "02x")

    return dense


if __name__ == "__main__":
    # Part 1
    print(knot_hash())

    # Part 2
    print(knot_hash(total=True))
