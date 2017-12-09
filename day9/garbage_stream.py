'''
https://adventofcode.com/2017/day/9
'''


def garbage_stream():
    chars = [ch for ch in open("input.txt").read()]
    skip, in_garbage = False, False
    depth, score, cleaned = 0, 0, 0

    for ch in chars:
        if skip:
            skip = False
        elif ch == '!':
            skip = True
        elif ch == '<':
            if in_garbage:
                cleaned += 1
            in_garbage = True
        elif ch == '>':
            in_garbage = False
        elif in_garbage:
            cleaned += 1
        elif ch == '{':
            depth += 1
        elif ch == '}':
            score += depth
            depth -= 1

    return cleaned, score


cleaned, score = garbage_stream()
# Part 1
print(score)
# Part 2
print(cleaned)
