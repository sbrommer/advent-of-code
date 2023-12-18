from itertools import permutations
from more_itertools import pairwise

# Parse input
lines = [line.split() for line in open(0)]

dists = {(l[0], l[2]): int(l[-1]) for l in lines}

dists.update({(to, frm): dist for (frm, to), dist in dists.items()})

cities = set.union(*map(set, dists))

# Get total distance for each permutation
total_dists = [sum(map(dists.get, pairwise(p)))
               for p in permutations(cities)]

# Get answers
print(min(total_dists), max(total_dists))
