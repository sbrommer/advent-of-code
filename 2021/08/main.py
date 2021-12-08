result = [line.split('|') for line in open(0)]

part1 = 0
part2 = 0
for s, o in result:
    p1 = [set(p) for p in s.split() if len(p) == 2][0]
    p4 = [set(p) for p in s.split() if len(p) == 4][0]

    n = ''
    for p in map(set, o.split()):
        l, l1, l4 = map(len, [p, p & p1, p & p4])

        part1 += l in [2, 3, 4 ,7]

        if   l  == 2: n += '1'
        elif l  == 4: n += '4'
        elif l  == 3: n += '7'
        elif l  == 7: n += '8'
        elif l4 == 4: n += '9'
        elif l4 == 2: n += '2'
        elif l  == 5: n += '3' if l1 == 2 else '5'
        elif l1 == 1: n += '6'
        else:         n += '0'
    part2 += int(n)

print(part1)
print(part2)
