start, _, *diagram = open(0)

splits = 0
beams = [c == 'S' for c in start]

for line in diagram[::2]:
    new_beams = [0] * len(beams)

    for i in range(len(beams)):
        if beams[i]:
            match line[i]:
                case '.':
                    new_beams[i] += beams[i]

                case '^':
                    splits += 1
                    new_beams[i-1] += beams[i]
                    new_beams[i+1] += beams[i]

    beams = new_beams

print(splits, sum(beams))
