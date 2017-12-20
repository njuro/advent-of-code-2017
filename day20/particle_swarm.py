'''
https://adventofcode.com/2017/day/20
'''

import operator
import re

regexp = re.compile(r'\w=<\s*([-]?\w+),([-]?\w+),([-]?\w+)>')


class Particle:
    __slots__ = ['index', 'position', 'velocity', 'acceleration']

    def __init__(self, index, data):
        self.index = index
        self.position = tuple(map(int, regexp.match(data[0]).groups()))
        self.velocity = tuple(map(int, regexp.match(data[1]).groups()))
        self.acceleration = tuple(map(int, regexp.match(data[2]).groups()))

    def update(self):
        self.velocity = tuple(map(operator.add, self.velocity, self.acceleration))
        self.position = tuple(map(operator.add, self.position, self.velocity))

    def distance(self):
        return sum(map(abs, self.position))

    def __eq__(self, other):
        return self.position == other.position

    def __hash__(self):
        return hash(self.position)

    def __str__(self):
        return "[Index: {}, Position: {}, Velocity: {}, Acceleration: {}]" \
            .format(self.index, self.position, self.velocity, self.acceleration)


def particle_swarm(collisions=False):
    particles = [Particle(index, data.strip().split(", ")) for index, data in
                 enumerate([line for line in open("input.txt").readlines()])]

    for _ in range(50 if collisions else 500):
        if collisions:
            # Remove collisions
            particles = list(filter(lambda p: particles.count(p) == 1, particles))

        # Update particles
        for p in particles:
            p.update()

    # Sort by distance
    particles.sort(key=lambda p: p.distance())
    return len(particles) if collisions else particles[0].index


# Part 1
print(particle_swarm())
# Part 2
print(particle_swarm(collisions=True))
