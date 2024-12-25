cat = ''.join

grid, moves = open(0).read().split('\n\n')

dirs = {'v': 1j, '^': -1j, '<': -1, '>': 1}
moves = [dirs[m] for m in cat(moves.split())]


def parse(grid, part2=False):
    if part2:
        trans = str.maketrans({'#': '##', 'O': '[]', '.': '..', '@': '@.'})
        grid = grid.translate(trans)

    return {x+y*1j: c
            for y, l in enumerate(grid.split())
            for x, c in enumerate(l)}


def movable(grid, p, d):
    p += d

    if grid[p] == '#':
        return False

    if grid[p] == '.':
        return True

    if grid[p] == '[' and d in [-1j, 1j]:
        return movable(grid, p, d) and movable(grid, p+1, d)

    if grid[p] == ']' and d in [-1j, 1j]:
        return movable(grid, p, d) and movable(grid, p-1, d)

    return movable(grid, p, d)


def move(grid, p, d):
    p += d

    if grid[p] == '[' and d in [-1j, 1j]:
        move(grid, p+1, d)

    if grid[p] == ']' and d in [-1j, 1j]:
        move(grid, p-1, d)

    if grid[p] != '.':
        move(grid, p, d)

    grid[p], grid[p-d] = grid[p-d], '.'


def gps(grid):
    return int(sum(100*p.imag+p.real for p, c in grid.items() if c in 'O['))


def run(grid):
    for m in moves:
        robot, = [p for p, c in grid.items() if c == '@']

        if movable(grid, robot, m):
            move(grid, robot, m)

    return gps(grid)


print(run(parse(grid)), run(parse(grid, True)))
