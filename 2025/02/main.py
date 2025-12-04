from itertools import chain
from re import findall

ids = [*chain(*[range(int(l), int(h)+1) for l, h in
                findall(r'(\d+)-(\d+)', open(0).read())])]


def is_invalid(i, part2=False):
    i = str(i)
    L = len(i)

    M = L+1 if part2 else 3

    return any(l*i[:L//l] == i for l in range(2, M))



print(sum(filter(is_invalid, ids)))
print(sum(i for i in ids if is_invalid(i, part2=True)))
