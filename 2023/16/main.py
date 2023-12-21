import sys

sys.setrecursionlimit(110 * 110)

grid = {complex(r, c): char
        for r, row in enumerate(open(0))
        for c, char in enumerate(row.strip())}


def run(p, d):
    seen = set()
    queue = [(p, d)]

    while queue:
        p, d = queue.pop()

        if (p, d) not in seen and p in grid:
            seen.add((p, d))

            ds = set()

            match grid[p]:
                case '\\': ds |= {1j / d}
                case '/':  ds |= {-1j / d}
                case '-':  ds |= {-1j, 1j}
                case '|':  ds |= {-1, 1}
                case _:    ds |= {d}

            queue += [(p + d, d) for d in ds]

    return len(set(p for p, _ in seen))


print(run(0, 1j))
print(max(run(p, d) for p in grid \
      for d in {1, -1, 1j, -1j} if p - d not in grid))
