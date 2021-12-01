from itertools import permutations
from parse import parse


# Helper functions
def longest_path(V, E):
    paths = set()
    for p in permutations(V):
        neighbours = zip(p, list(p[1:]) + [p[0]])
        paths.add(sum(E[v][w] + E[w][v] for v, w in neighbours))
    return max(paths)


# Parse input
lines = open(0).readlines()

graph = {}
attendees = set()

for line in lines:
    a, gl, n, b = parse('{} would {} {} happiness units by sitting next to {}.\n',
                        line)

    attendees |= set([a, b])

    if a not in graph:
        graph[a] = {}

    graph[a][b] = ((gl == 'gain') * 2 - 1) * int(n)

# Part 1
happiness = longest_path(attendees, graph)
print(happiness)

# Part 2
graph['me'] = {}

for a in attendees:
    graph[a]['me'] = 0
    graph['me'][a] = 0

attendees.add('me')

happiness2 = longest_path(attendees, graph)
print(happiness2)
