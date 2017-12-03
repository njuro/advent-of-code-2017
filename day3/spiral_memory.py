'''
https://adventofcode.com/2017/day/3
'''

from itertools import cycle


def generate_spiral(max, adjacent=False):
    # order of directions
    directions = cycle(['R', 'U', 'L', 'D'])

    coords = []
    for _ in range(4):
        # initialize quadrants
        coords.append([[]])

    # initialize origin and variables
    put_value(coords, 0, 0, 1)
    value = 1
    shift, x, y = 0, 0, 0

    while True:
        # pick new direction
        direction = next(directions)
        if direction in ('R', 'L'):
            # if the new direction is Right or Left, we need to make one more step
            shift += 1

        # make [shift] moves in that direction
        for _ in range(shift):
            # check if we aren't done
            if (not adjacent and value >= max) or (adjacent and value > max):
                return coords, x, y, value

            # change coordinates based on direction
            if direction == 'R':
                x += 1
            elif direction == 'U':
                y += 1
            elif direction == 'L':
                x -= 1
            else:
                y -= 1

            # calculate new value
            if adjacent:
                neighbors = (
                    (x, y + 1), (x + 1, y + 1), (x + 1, y), (x + 1, y - 1), (x, y - 1), (x - 1, y - 1), (x - 1, y),
                    (x - 1, y + 1))
                # sum of all neighborging values
                value = sum([get_value(coords, n[0], n[1]) for n in neighbors])
            else:
                value += 1

            put_value(coords, x, y, value)


def get_quadrant(x, y):
    if x >= 0 and y >= 0:
        return 0
    elif x < 0 and y >= 0:
        return 1
    elif x < 0 and y < 0:
        return 2
    else:
        return 3


def put_value(coords, x, y, value):
    # print("Putting {} at X: {}, Y: {}".format(value, x, y))
    # get quadrant for coordinates
    quadrant = coords[get_quadrant(x, y)]
    x, y = abs(x), abs(y)

    # resize quadrant if necessary
    if x >= len(quadrant) - 1:
        quadrant.append([])
    if y >= len(quadrant[x]) - 1:
        for i in range(len(quadrant[x]) - 1, y):
            quadrant[x].append(0)

    quadrant[x][y] = value


def get_value(coords, x, y):
    try:
        # get quadrant for coordinates
        quadrant = coords[get_quadrant(x, y)]
        x, y = abs(x), abs(y)

        return quadrant[x][y]
    except IndexError as ie:
        # this field is not initalized yet, therefore we return 0
        return 0


def spiral_memory(max, adjacent=False):
    coords, x, y, value = generate_spiral(max, adjacent)
    if adjacent:
        return "First value larger as {} is {}.".format(max, value)
    else:
        return "{} is {} steps from the middle.".format(max, (abs(x) + abs(y)))


max_value = 36807800
# Part 1
print(spiral_memory(max_value))
# Part 2
# print(spiral_memory(max_value, adjacent=True))
