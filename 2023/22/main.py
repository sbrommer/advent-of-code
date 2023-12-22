import numpy as np
import re

# Parse
stack = [[*map(int, re.findall(r'\d+', line))] for line in open(0)]
stack = sorted(stack, key=lambda b: b[2])

X = max(*[b[0] for b in stack]) + 1
Y = max(*[b[1] for b in stack]) + 1

stack = [[slice(b[0], b[3]+1), slice(b[1], b[4]+1),
          b[5] - b[2] + 1] for b in stack]  # (x-slice, y-slice, height)


# Fall
heightmap = np.zeros((X, Y))
topview = np.empty((X, Y)); topview[:] = -1
below = dict()

for i, (x, y, h) in enumerate(stack):
    m = heightmap[x, y].max()

    below[i] = set(topview[x, y][heightmap[x, y] == m])

    heightmap[x, y] = m + h
    topview[x, y] = i

above = {a: set([b for b, v in below.items() if a in v]) for a in below}


def disintegrate(i):
    fallen = set()
    queue = [i]
    while queue:
        i = queue.pop()
        fallen |= {i}
        queue += [a for a in above[i] if not below[a] - fallen]
    return fallen


save = set(below) - \
       set.union(*[b for b in below.values() if len(b) == 1])

print(len(save), sum(len(disintegrate(i)) - 1 for i in below))
