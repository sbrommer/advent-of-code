import re
from operator import add, mul


def parse(text=open(0)):
    def parse_line(line):
        tv, *ns = map(int, re.findall(r'\d+', line))
        return tv, ns

    return [*map(parse_line, text)]


def cat(n, m):
    return int(str(n)+str(m))


def solvable(tv, ns, ops):
    def solvable_(ns, acc):
        if not ns:
            return acc == tv

        return any(solvable_(ns[1:], op(acc, ns[0])) for op in ops)

    return solvable_(ns[1:], ns[0])


def calibrate(equations, part1=True):
    ops = [add, mul] if part1 else [add, mul, cat]
    return sum(tv * solvable(tv, ns, ops) for tv, ns in equations)


equations = parse()
print(calibrate(equations), calibrate(equations, False))
