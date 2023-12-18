from itertools import starmap
from parse import findall

T = 2503


def distance(speed, t_fly, t_rest, t=T):
    n, r = divmod(t, t_fly + t_rest)

    return (n * t_fly + min(r, t_fly)) * speed


# Parse data
data = [*findall('{:d} km/s for {:d} seconds, but then must rest for {:d}',
                 open(0).read())]

# Part 1
print(max(starmap(distance, data)))

# Part 2
races = [[distance(*deer, t+1) for t in range(T)] for deer in data]
snapshots = zip(*races)

winners = [deer for s in snapshots
           for deer, dist in enumerate(s)
           if dist == max(s)]

print(max(map(winners.count, set(winners))))
