start, _, *diagram = open(0)

splits = 0
beams = [c == 'S' for c in start]

for line in diagram[::2]:
    for i in range(len(beams)):
        if beams[i] and line[i] == '^':
            splits += 1
            beams[i-1] += beams[i]
            beams[i+1] += beams[i]
            beams[i] = 0

print(splits, sum(beams))
