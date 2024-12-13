from re import findall
from more_itertools import chunked


def parse(text=open(0).read()):
    ints = [*map(int, findall(r'\d+', text))]
    return [*chunked(ints, 6)]


def cost(machines, part2=False):
    c = 0
    for ax, ay, bx, by, px, py in machines:
        if part2:
            px += 10_000_000_000_000
            py += 10_000_000_000_000

        a = (by*px-bx*py) / (by*ax-bx*ay)
        b = (ay*px-ax*py) / (ay*bx-ax*by)

        if not (a % 1 or b % 1):
            c += 3*a+b
    return int(c)


machines = parse()

print(cost(machines), cost(machines, True))
