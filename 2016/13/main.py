def is_open(x, y):
    n = x*x + 3*x + 2*x*y + y + y*y
    n += 1362
    b = bin(n)
    c = b.count('1')
    return not bool(c % 2)


def neighbours(x, y):
    ns = set([(x+1, y), (x, y+1)])
    if x > 0:
        ns.add((x-1, y))
    if y > 0:
        ns.add((x, y-1))
    return ns


# Ρart 1
visited, visiting = set(), set([(1, 1)])
n = 0
while (31, 39) not in visiting:
    n += 1
    visited |= visiting
    visiting = set.union(*[neighbours(*loc) for loc in visiting])
    visiting = set([loc for loc in visiting if is_open(*loc)])
    visiting -= visited

print(n)

# Part 2
visited, visiting = set(), set([(1, 1)])
for n in range(51):
    visited |= visiting
    visiting = set.union(*[neighbours(*loc) for loc in visiting])
    visiting = set([loc for loc in visiting if is_open(*loc)])
    visiting -= visited

print(len(visited))
