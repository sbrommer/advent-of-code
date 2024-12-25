from itertools import combinations, accumulate

D = {x+y*1j: c
     for y, l in enumerate(open(0))
     for x, c in enumerate(l.strip())}

S, = [p for p, c in D.items() if c == 'S']
E, = [p for p, c in D.items() if c == 'E']
ps = [p for p, c in D.items() if c != '#']


steps = [0]
while (p := S + sum(steps)) != E:
    steps += [d for d in [-1, 1, -1j, 1j] if d != -steps[-1] and p+d in ps]

dists = [*enumerate(accumulate(steps[1:], initial=S))]

cheats1, cheats2 = 0, 0

for (d1, p1), (d2, p2) in combinations(dists, 2):
    d = int(abs(p1.real-p2.real) + abs(p1.imag-p2.imag))
    cheats1 += d <=  2 and d2-d1-d >= 100
    cheats2 += d <= 20 and d2-d1-d >= 100

print(cheats1, cheats2)
