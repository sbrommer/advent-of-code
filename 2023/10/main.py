from collections import defaultdict


def shoelace(x, y):
    return int(x.real * y.imag - x.imag * y.real)


U, D, R, L = -1, 1, 1j, -1j

turns = defaultdict(lambda: {U: U, D: D, L: L, R: R})
turns.update({'F': {U: R, L: D}, '7': {R: D, U: L},
              'J': {D: L, R: U}, 'L': {D: R, L: U}})

pipes = defaultdict(lambda: '.')
pipes.update({complex(r, c): pipe
             for r, line in enumerate(open(0))
             for c, pipe in enumerate(line)})

connected = [(U, '|F7'), (D, '|JL'), (R, '-FL'), (L, '-7J')]

p = [p for p, pipe in pipes.items() if pipe == 'S'][0]
d = [d for d, cs in connected if pipes[p + d] in cs][0]

steps = 0
area = 0

while pipes[p] != 'S' or not steps:
    steps += 1
    area += shoelace(p, p + d)

    p += d
    d = turns[pipes[p]][d]

print(steps // 2, abs(area // 2) + 1 - steps // 2)
