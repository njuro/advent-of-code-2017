'''
https://adventofcode.com/2017/day/24
'''


def bridge():
    components = [(int(x), int(y)) for x, y in [line.split("/") for line in open("input.txt").readlines()]]
    components.extend([c[::-1] for c in components])
    bridges = {}

    def create_bridges(bridge, available, strength=0):
        head = bridge[-1]
        available.remove(head)
        available.remove(head[::-1])
        strength += sum(head)

        compatible = list(filter(lambda a: a[0] == head[1] and a not in bridge, available))
        if len(compatible) == 0:
            bridges[strength] = bridge
        for c in compatible:
            bridge.append(c)
            create_bridges(bridge[:], available[:], strength)

    for port in list(filter(lambda p: p[0] == 0, components)):
        create_bridges([port], components)

    max_length = len(max(bridges.values(), key=len))
    longest = {k: v for k, v in bridges.items() if len(v) == max_length}
    return max(bridges.keys()), max(longest.keys())


strongest, longest = bridge()
# Part 1
print(strongest)
# Part 2
print(longest)
