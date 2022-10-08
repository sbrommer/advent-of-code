from parse import search


def parse_disc(line):
    d, m, p = search('Disc #{:d} has {:d} positions; at time=0, it is at position {:d}.', line)
    return d, m, p


def get_position(t, d, m, p):
    return (p + t + d) % m


discs = [parse_disc(line) for line in open(0).readlines()]


time = 0
while any([get_position(time, *disc) for disc in discs]):
    time += 1

print(time)
