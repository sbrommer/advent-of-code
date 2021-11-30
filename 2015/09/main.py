from sys import stdin
from itertools import permutations
from parse import *

# Parse input
cities = set()
dists = {}

line = stdin.readline().strip()
while len(line):
    frm, to, dist = parse('{} to {} = {:d}', line)

    dists[(frm, to)] = dist
    dists[(to, frm)] = dist

    cities = cities.union([frm, to])

    line = stdin.readline().strip()

# Get total distance for each permutation
total_dists = set()
for p in permutations(cities):
    route = zip(p, p[1:])
    total_dists.add(sum(dists[r] for r in route))

# Get answers
print(min(total_dists))
print(max(total_dists))
