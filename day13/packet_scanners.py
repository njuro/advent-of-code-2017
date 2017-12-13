'''
https://adventofcode.com/2017/day/13
'''


def is_caught(depth, size, delay=0):
    return (delay + depth) % (2 * size - 2) == 0


def simulate_delay(firewalls, delay):
    for depth, size in firewalls.items():
        if is_caught(depth, size, delay):
            return False
    return True


firewalls = {int(depth): int(size) for depth, size in
             [line.split(": ") for line in open("input.txt").readlines()]}

# Part 1
print(sum([depth * size for depth, size in firewalls.items() if is_caught(depth, size)]))

# Part 2
delay = 0
while not simulate_delay(firewalls, delay):
    delay += 1
print(delay)
