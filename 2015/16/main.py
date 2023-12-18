from itertools import starmap
from parse import findall

tape = {'children': 3, 'cats': 7, 'samoyeds': 2, 'pomeranians': 3,
        'akitas': 0, 'vizslas': 0, 'goldfish': 5, 'trees': 3,
        'cars': 2, 'perfumes': 1}


sues = {}
results = findall('Sue {:d}: {:w}: {:d}, {:w}: {:d}, {:w}: {:d}',
                  open(0).read())


sues = {sue: {c1: int(n1), c2: int(n2), c3: int(n3)}
        for sue, c1, n1, c2, n2, c3, n3 in results}

for sue, compounds in sues.items():
    if all(tape[c] == n for c, n in compounds.items()):
        print(sue)


def match(c, n):
    if c in ['cats', 'trees']:
        return tape[c] < n
    if c in ['pomeranians', 'goldfish']:
        return tape[c] > n
    return tape[c] == n


for sue, compounds in sues.items():
    if all(starmap(match, compounds.items())):
        print(sue)
