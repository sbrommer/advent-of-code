from sys import stdin
from re import search
import numpy as np

lines = stdin.readlines()

def parse_line(line):
    op, x1, y1, x2, y2 = search('(\w+) (\d+),(\d+) through (\d+),(\d+)', line).groups()
    return op, slice(int(x1), int(x2)+1), slice(int(y1), int(y2)+1)

# part 1
lights = np.zeros((1000, 1000), dtype = np.bool)

for line in lines:
    op, sx, sy = parse_line(line)
    if op == 'toggle':
        lights[sx, sy] ^= bool(1)
    elif op == 'on':
        lights[sx, sy] = 1
    else: # op == 'off'
        lights[sx, sy] = 0

print(sum(sum(lights)))

# part 2
lights = np.zeros((1000, 1000), dtype = int)

for line in lines:
    op, sx, sy = parse_line(line)
    if op == 'toggle':
        lights[sx, sy] += 2
    elif op == 'on':
        lights[sx, sy] += 1
    else: # op == 'off'
        lights[sx, sy] -= 1
    lights[lights < 0] = 0

print(sum(sum(lights)))
