'''
https://adventofcode.com/2017/day/17
'''


def spinlock(part2=False):
    answer, position, size, step = 0, 0, 1, 370
    buffer = [0]
    max_val = 50 * 10 ** 6 if part2 else 2017
    for i in range(1, max_val + 1):
        position = (position + step) % size + 1
        if part2:
            if position == 1:
                answer = i
        else:
            buffer = buffer[:position] + [i] + buffer[position:]
        size += 1

    return answer if part2 else buffer[buffer.index(max_val) + 1]


# Part 1
print(spinlock())
# Part 2
print(spinlock(part2=True))
