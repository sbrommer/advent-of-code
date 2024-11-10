from collections import defaultdict

# parse input
inp = [line.strip() for line in open(0).readlines()]

grid1 = defaultdict(int)
grid2 = defaultdict(int)

for r, row in enumerate(inp, start=-(len(inp)//2)):
    for c, char in enumerate(row, start=-(len(row)//2)):
        grid1[r+c*1j] = char == '#'
        grid2[r+c*1j] = 2 * (char == '#')


def bursts(grid, part=1):
    n_status = part * 2
    p, d = 0, -1
    infections = 0

    for _ in range(10000 if part == 1 else 10000000):
        # update direction
        if grid[p] == 0:
            d *= 1j
        elif grid[p] == part:
            d *= -1j
        elif grid[p] == 3:
            d *= -1

        # update status
        grid[p] = (grid[p] + 1) % n_status

        # count infections
        infections += grid[p] == part

        # update position
        p += d

    return infections


print(bursts(grid1), bursts(grid2, 2))
