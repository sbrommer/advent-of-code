def taxicab(p):
    return int(abs(p.real) + abs(p.imag))


instructions = [([-1j, 1j][i[0] == 'R'], int(i[1:]))
                for i in input().split(', ')]

pos, dir = 0, 1
visited = {pos}
hq = None

for turn, steps in instructions:
    dir *= turn
    for _ in range(steps):
        pos += dir
        if pos in visited:
            hq = hq or pos
        visited |= {pos}

print(taxicab(pos), taxicab(hq))
