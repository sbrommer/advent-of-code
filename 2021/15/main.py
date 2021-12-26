import heapq

# Parse
cave = [[*map(int, line.strip())] for line in open(0)]

h, w = len(cave), len(cave[0])


# Helper functions
def neighbours(x, y, t):
    nbs = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
    def is_valid(nb): return nb[0] in range(w * t) and nb[1] in range(h * t)
    return set(filter(is_valid, nbs))


# Only works if t <= 5.
def local_risk(x, y):
    risk = cave[y % h][x % w] + y // h + x // w
    return risk % 9 or 9


# Shortest path algorithm
def dijkstra(n_tiles=1):
    # Constants
    start = (0, 0)
    end = (w * n_tiles - 1, h * n_tiles - 1)

    # Initialise
    queue = [(0, start)]
    visited = set([start])

    # Walk
    while queue:
        risk, node = heapq.heappop(queue)

        # Return if exit is found
        if node == end:
            return risk

        # Visit all unvisited neighbours
        for nb in neighbours(*node, n_tiles) - visited:
            visited.add(nb)
            heapq.heappush(queue, (risk + local_risk(*nb), nb))


# Part 1
print(dijkstra())

# Part 2
print(dijkstra(5))
