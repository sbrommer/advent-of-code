from re import findall
from operator import mul
from functools import reduce
import time


def prod(xs):
    return reduce(mul, xs, 1)


def parse_line(line):
    return [*map(int, findall(r'-?\d+', line))]


robots = [*map(parse_line, open(0))]
w, h = 101, 103


def simulate(robots, t):
    return [((px+t*vx)%w, (py+t*vy)%h)
            for px, py, vx, vy in robots]


def safety_factor(ps):
    return prod(sum(ps.count((x+dx, y+dy))
                    for dx in range(w//2)
                    for dy in range(h//2))
                for x in [0, w//2+1]
                for y in [0, h//2+1])


def print_grid(t):
    ps = simulate(robots, t)
    for y in range(h):
        for x in range(w):
            c = ps.count((x, y))
            print(c if c else '.', end='')
        print()
    print('Time:', t)


print_grid(7138)
print(safety_factor(simulate(robots, 100)))

# For experimentation:
# for t in range(31, 7139, 103):
#     print_grid(t)
#     time.sleep(1)
