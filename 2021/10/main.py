from functools import reduce
from statistics import median

# Constants
points1 = {')': 3, ']': 57, '}': 1197, '>': 25137}
points2 = {'(': 1, '[': 2,  '{': 3,    '<': 4}

closes   = set(')]}>')
brackets = ['()', '[]', '{}', '<>']


# Helper function
def match(l):
    while any(map(lambda b: b in l, brackets)):
        for b in brackets:
            l = l.replace(b, '')
    return l


# Calculate scores
score = 0
scores = []
for l in open(0):
    l = match(l.strip())
    if set(l) & closes: # Part 1
        score += points1[next(filter(lambda c: c in closes, l))]
    else: # Part 2
        scores.append(reduce(lambda s, c: s * 5 + points2[c], l[::-1], 0))

# Part 1
print(score)

# Part 2
print(median(scores))
