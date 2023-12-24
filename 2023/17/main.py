from heapq import heappop as pop, heappush as push


heat = {complex(r, c): int(loss)
        for r, row in enumerate(open(0))
        for c, loss in enumerate(row.strip())}

dest = [*heat][-1]


def dijkstra(min, max):
    visited = set()
    queue = [(0, (n := 0), 0, 1), (0, (n := 0), 0, 1j)]

    while queue:
        h, _, p, d = pop(queue)

        if p == dest:
            return h

        if (p, d) not in visited:
            for d_ in [1j/d, -1j/d]:
                for s in range(min, max + 1):
                    q = p + d_ * s
                    if q in heat.keys():
                        h_ = h + sum(heat[p + d_ * s_] for s_ in range(1, s+1))
                        push(queue, (h_, (n := n+1), q, d_))

            visited |= {(p, d)}


print(dijkstra(1, 3), dijkstra(4, 10))
