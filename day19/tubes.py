'''
https://adventofcode.com/2017/day/19
'''


def tubes():
    diagram = [line for line in open("input.txt").readlines()]
    steps, x, y = 0, 0, diagram[0].index("|")
    direction, buffer = 'S', str()

    while True:
        steps += 1
        neighbours = {
            'N': (x - 1, y),
            'S': (x + 1, y),
            'E': (x, y + 1),
            'W': (x, y - 1)
        }
        x, y = neighbours[direction]

        # move to next field and check if we are still in diagram
        try:
            current = diagram[x][y]
            if current.isspace():
                raise IndexError
        except IndexError:
            return buffer, steps

        if current == '+':
            # pick new direction
            if direction in ('N', 'S'):
                adj = ('E', 'W')
                dx, dy = x, y + 1
                n = '-'
            else:
                adj = ('N', 'S')
                dx, dy = x - 1, y
                n = '|'

            try:
                nxt = diagram[dx][dy]
                direction = adj[0] if nxt == n or nxt.isalpha() else adj[1]
            except IndexError:
                direction = adj[1]

        if current.isalpha():
            buffer += current


buffer, steps = tubes()
# Part 1
print(buffer)
# Part 2
print(steps)
