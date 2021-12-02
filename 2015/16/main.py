from itertools import starmap
from parse import findall

tape = {'children': 3, 'cats': 7, 'samoyeds': 2, 'pomeranians': 3,
        'akitas': 0, 'vizslas': 0, 'goldfish': 5, 'trees': 3,
        'cars': 2, 'perfumes': 1}


# Parse
sues = {}
results = findall('Sue {:d}: {:w}: {:d}, {:w}: {:d}, {:w}: {:d}',
                  open(0).read())

for sue, x1, n1, x2, n2, x3, n3 in results:
    sues[sue] = {x1: int(n1), x2: int(n2), x3: int(n3)}

# Part 1
for s, xs in sues.items():
    if all(tape[x] == n for x, n in xs.items()):
        print(s)


# Part 2
def match(x, n):
    if x in ['cats', 'trees']:
        return tape[x] < n
    if x in ['pomeranians', 'goldfish']:
        return tape[x] > n
    return tape[x] == n


for s, xs in sues.items():
    if all(starmap(match, xs.items())):
        print(s)
