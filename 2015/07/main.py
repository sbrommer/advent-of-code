from functools import cache


def parse_line(line):
    *ops, _, wire = line.split()
    return wire, ops


@cache
def evaluate(wire='a'):
    if wire.isdigit():
        return int(wire)

    ops = circuit[wire]

    if len(ops) == 1:
        return evaluate(ops[0])

    if len(ops) == 2:
        return ~evaluate(ops[1])

    l, r = evaluate(ops[0]), evaluate(ops[2])

    match ops[1]:
        case 'AND':
            return l & r

        case 'OR':
            return l | r

        case 'LSHIFT':
            return l << r

        case 'RSHIFT':
            return l >> r


circuit = dict(map(parse_line, open(0)))

print(a := evaluate(), end=' ')

circuit['b'] = [str(a)]
evaluate.cache_clear()
print(evaluate())
