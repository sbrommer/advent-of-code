# run with pypy!

def disk(blocks):
    for i in range(len(blocks))[::-1]:
        for j in range(i):
            datai, ni = blocks[i]
            dataj, nj = blocks[j]
            if 0 < ni <= nj and datai and not dataj:
                blocks[i] = (0, ni)
                blocks[j] = (0, (nj - ni))
                blocks.insert(j, (datai, ni))

    return sum(([t] * l for t, l in blocks), [])


def checksum(disk):
    return sum(i*(n-1) for i, n in enumerate(disk) if n)


diskmap = [*map(int, input())]

blocks1 = [t for i, n in enumerate(diskmap, 2)
             for t in [(0 if i % 2 else i // 2, 1)] * n]

blocks2 = [(0 if i % 2 else i // 2, n)
           for i, n in enumerate(diskmap, 2)]

print(checksum(disk(blocks1)), checksum(disk(blocks2)))
