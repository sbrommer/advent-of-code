rolls = {x+y*1j for y, r in enumerate(open(0))
                for x, c in enumerate(r)
                if c == '@'}


def neigbours(p):
    return {p+d for d in [-1-1j, -1j, 1-1j, -1, 1, -1+1j, 1j, 1+1j]}


def get_accessable(rolls):
    return {r for r in rolls if len(neigbours(r) & rolls) < 4}


total = 0

while accessable := get_accessable(rolls):
    if not total:
        print(len(accessable))

    total += len(accessable)
    rolls -= accessable

print(total)
