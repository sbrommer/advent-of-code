from itertools import permutations
from parse import parse


def longest_path(V, E):
    paths = set()
    for p in permutations(V):
        neighbours = zip(p, p[1:] + p)
        paths.add(sum(E[v][w] + E[w][v] for v, w in neighbours))
    return max(paths)


graph = {}
attendees = set()

for line in open(0):
    a, gl, h, b = parse('{} would {} {} happiness units by sitting next to {}.\n',
                        line)

    attendees |= set([a, b])

    if a not in graph:
        graph[a] = {}

    graph[a][b] = ((gl == 'gain') * 2 - 1) * int(h)

# Part 1
print(longest_path(attendees, graph))

# Part 2
graph['me'] = {}

for a in attendees:
    graph[a]['me'] = 0
    graph['me'][a] = 0

attendees.add('me')

print(longest_path(attendees, graph))
