from re import search
import numpy as np


def parse_line(line):
    op, *cs = search(r'(\w+) (\d+),(\d+) through (\d+),(\d+)', line).groups()
    x1, y1, x2, y2 = map(int, cs)
    return op, (slice(int(x1), int(x2)+1), slice(int(y1), int(y2)+1))


instructions = [*map(parse_line, open(0))]

lights1 = np.zeros((1000, 1000), dtype=bool)
lights2 = np.zeros((1000, 1000), dtype=int)

for op, s in instructions:
    if op == 'toggle':
        lights1[s] ^= True
        lights2[s] += 2
    elif op == 'on':
        lights1[s] = True
        lights2[s] += 1
    else:  # op == 'off'
        lights1[s] = False
        lights2[s] -= 1
    lights2[lights2 < 0] = 0

print(sum(sum(lights1)), sum(sum(lights2)))
