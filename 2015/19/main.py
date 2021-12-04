import re
from parse import search

# Parse
lines = open(0).readlines()

m = re.findall(r'[A-Z][^A-Z]*', lines[-1].strip())

rs = {}
for (a, p) in [search('{:w} => {:w}', r) for r in lines[:-2]]:
    rs[a] = rs.get(a, set())
    rs[a].add(p)

# Part 1
ms = set()
for i, a in enumerate(m):
    if a in rs:
        for r in rs[a]:
            m2 = m.copy()
            m2[i] = r
            ms.add(''.join(m2))
print(len(ms))

# Part 2
a = len(m)
rn = m.count('Rn')
ar = m.count('Ar')
y = m.count('Y')
print(a - rn - ar - y * 2 - 1)
