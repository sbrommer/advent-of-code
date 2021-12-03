from itertools import product

# Parse
lights_on = {(x, y) for y, l in enumerate(open(0))
                    for x, c in enumerate(l)
                    if c == '#'}


# Helper functions / variables
bulbs = set(product(range(100), range(100)))
corners = {(0, 0), (0, 99), (99, 0), (99, 99)}

def neighbours(x, y):
    return {(x+dx, y+dy) for (dx, dy) in
            ((-1, -1), (-1, 0), (-1, 1),
              (0, -1),           (0, 1),
              (1, -1),  (1, 0),  (1, 1))}


def solve(lights_on, corners={}):
    def new_state(bulb):
        n = len(neighbours(*bulb) & lights_on)
        return any((bulb in lights_on and n == 2, n == 3, bulb in corners))

    for i in range(100):
        lights_on  = set(filter(new_state, bulbs))

    return len(lights_on)


# Part 1
print(solve(lights_on))

# Part 2
print(solve(lights_on | corners, corners))
