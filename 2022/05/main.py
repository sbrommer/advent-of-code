from parse import parse


def parse_crates(input):
    lines = input.split('\n')[:-1]

    crates = [line[1::4] for line in lines]

    stacks = zip(*crates)

    return [''.join(stack).strip() for stack in stacks]


o = open(0).read()
crates, procedure = o.split('\n\n')

crates1 = parse_crates(crates)
crates2 = list(crates1)

for step in procedure.split('\n')[:-1]:
    n, s1, s2 = parse('move {:d} from {:d} to {:d}', step.strip())

    # Part 1
    for _ in range(n):
        crates1[s2-1] = crates1[s1-1][0] + crates1[s2-1]
        crates1[s1-1] = crates1[s1-1][1:]

    # Part 2
    crates2[s2-1] = crates2[s1-1][:n] + crates2[s2-1]
    crates2[s1-1] = crates2[s1-1][n:]

print(''.join(crate[0] for crate in crates1))
print(''.join(crate[0] for crate in crates2))
