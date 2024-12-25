from itertools import combinations

schematics = [{i for i, c in enumerate(s) if c == '#'}
              for s in open(0).read().split('\n\n')]

print(sum(not(s & t) for s, t in combinations(schematics, 2)))
