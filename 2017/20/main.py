import re
from more_itertools import chunked


def parse(text=open(0)):
    return [*map(parse_line, text)]


def parse_line(line):
    return tuple(map(tuple, chunked(parse_ints(line), 3)))


def parse_ints(str):
    return map(int, re.findall(r'-?\d+', str))


def min_index(xs, key):
    return min(enumerate(xs), key=lambda e: key(e[1]))[0]


def total_acc(p):
    return sum(map(abs, p[2]))


def slowest_particle(particles):
    # assumes no particles have the same total acceleration
    return min_index(particles, key=total_acc)


def addt(tuples):
    return tuple(map(sum, zip(*tuples)))


def update(p):
    return (addt(p), addt(p[1:]), p[2])


def converge(ps):
    # assumes all collisions occur within 50 ticks
    ps = set(ps)

    for _ in range(50):
        collided = {p1 for p1 in ps for p2 in ps - {p1} if p1[0] == p2[0]}

        ps = {*map(update, ps - collided)}

    return len(ps)


particles = parse()

print(slowest_particle(particles),
      converge(particles))
