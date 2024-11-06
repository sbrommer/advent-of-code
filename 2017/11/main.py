from itertools import accumulate


def sign(n):
    return 1 if n > 0 else -1 if n < 0 else 0


def manhattan(q):
    x, y = q.real, q.imag
    if sign(x) == sign(y):
        return abs(x + y)
    return int(max(abs(x), abs(y)))


def step(pos, dpos):
    steps = {'n': -1+1j, 'ne': 0+1j, 'se':  1,
             's':  1-1j, 'sw': 0-1j, 'nw': -1}

    return pos + steps[dpos]


path = input().split(',')
positions = [*accumulate(path, step, initial=0+0j)]

print(manhattan(positions[-1]), max(map(manhattan, positions)))
