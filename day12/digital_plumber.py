'''
https://adventofcode.com/2017/day/12
'''


def digital_plumber():
    pipes = {f: t.split(",") for f, t in
             [line.replace(' ', '').strip().split("<->") for line in open("input.txt").readlines()]}
    seen, groups = [], []

    for key in pipes.keys():
        if key in seen:
            continue

        queue = [key]
        connected = []
        while len(queue) > 0:
            key = queue.pop(0)
            connected.append(key)
            for value in pipes[key]:
                if value not in connected:
                    queue.append(value)

        groups.append(connected)
        seen.extend(connected)

    return groups


groups = digital_plumber()
# Part 1
print(len(groups[0]))
# Part 2
print(len(groups))
