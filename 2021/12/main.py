from collections import defaultdict

# Parse
edges = defaultdict(set)
for connection in open(0):
    a, b = connection.strip().split('-')
    if b != 'start':
        edges[a].add(b)
    if a != 'start':
        edges[b].add(a)


# DFS
def dfs(cave='start', visited=set(), bonus=False):
    if cave == 'end':
        return 1

    if cave in visited:
        if cave.islower():
            if not bonus:
                return 0
            bonus = False

    return sum(dfs(adj, visited | {cave}, bonus) for adj in edges[cave])


# Part 1
print(dfs())

# Part 2
print(dfs(bonus=True))
