from parse import findall
from collections import Counter

# Parse
instr = open(0).read()
template = instr.split('\n')[0]
rules = dict(findall('{:w} -> {:w}', instr))

# Initialise
pairs = Counter([l + r for l, r in zip(template, template[1:])])
elements = Counter(template)

# Calculate
for n in [10, 40]:
    for _ in range(n):
        for (l, r), c in pairs.copy().items():
            m = rules[l + r]
            pairs[l + r] -= c
            pairs[l + m] += c
            pairs[m + r] += c
            elements[m] += c

    print(max(elements.values()) - min(elements.values()))

