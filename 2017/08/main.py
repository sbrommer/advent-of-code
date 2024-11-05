from collections import defaultdict


def parse_line(line):
    reg, inc_dec, d, _, *condition = line.split()

    d = int(d) * (1 if inc_dec == 'inc' else -1)

    return reg, d, condition


def eval_(registers, condition):
    condition[0] = str(registers[condition[0]])
    return eval(''.join(condition))


instructions = [parse_line(line) for line in open(0).readlines()]

registers = defaultdict(int)
highest = 0

for reg, d, condition in instructions:
    if eval_(registers, condition):
        registers[reg] += d
        highest = max(highest, max(registers.values()))

print(max(registers.values()), highest)
