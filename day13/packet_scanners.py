'''
https://adventofcode.com/2017/day/13
'''


class Firewall:
    def __init__(self, depth, size):
        self.depth = depth
        self.size = size
        self.scanner = 0
        self.forward = False

    def move(self):
        if self.scanner == 0:
            self.forward = True
        if self.scanner == self.size - 1:
            self.forward = False
        self.scanner += 1 if self.forward else -1


def calculate_score(firewalls):
    score = 0

    for position in range(max(firewalls.keys()) + 1):
        if position in firewalls.keys():
            firewall = firewalls[position]
            if firewall.scanner == 0:
                score += position * firewall.size
        for fw in firewalls.values():
            fw.move()

    return score


def simulate_delay(firewalls, delay):
    for fw in firewalls.values():
        if (delay + fw.depth) % (2 * fw.size - 2) == 0:
            return False
    return True


firewalls = {int(depth): Firewall(int(depth), int(size)) for depth, size in
             [line.split(": ") for line in open("input.txt").readlines()]}

# Part 1
print(calculate_score(firewalls))

# Part 2
delay = 0
while not simulate_delay(firewalls, delay):
    delay += 1
print(delay)
