from parse import search


def parse_disc(line):
    d, m, p = search('Disc #{:d} has {:d} positions; at time=0, it is at position {:d}.', line)
    return d, m, p


def get_position(t, d, m, p):
    return (p + t + d) % m


def best_time(discs):
    time = 0

    while any(get_position(time, *disc) for disc in discs):
        time += 1

    return time


discs = [*map(parse_disc, open(0))]
disc = [7, 11, 0]

print(best_time(discs), best_time(discs + [disc]))
