from re import findall
from collections import defaultdict

lines = open(0).readlines()

m = findall(r'[A-Z][^A-Z]*', lines[-1].strip())

rs = defaultdict(lambda: set())
for a, c in [l.strip().split(' => ') for l in lines[:-2]]:
    rs[a].add(c)

# Part 1
ms = set()
for i, a in enumerate(m):
    if a in rs:
        for r in rs[a]:
            copy_ = m.copy()
            copy_[i] = r
            ms.add(''.join(copy_))
print(len(ms))

# Part 2
l = len(m)
Rn = m.count('Rn')
Ar = m.count('Ar')
Y = m.count('Y')
print(l - Rn - Ar - Y * 2 - 1)
