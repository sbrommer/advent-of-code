from itertools import accumulate
from more_itertools import distribute


def visited(directions):
    return set(accumulate(directions))


d_map = {'<': -1j, '>': 1j, '^': -1, 'v': 1}
directions = [*map(d_map.get, input())]

print(len(visited(directions)),
      len(set.union(*map(visited, distribute(2, directions)))))
