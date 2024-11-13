from collections import defaultdict

Is = [line.split() for line in open(0)]


def run(Is, c=0):
    regs = defaultdict(int)
    regs['c'] = c

    def eval(x):
        try:
            return int(x)
        except ValueError:
            return regs[x]

    i = 0

    while i < len(Is):
        instr, *args = Is[i]
        x, y = args[0], args[-1]

        match instr:
            case 'cpy': regs[y] = eval(x)
            case 'inc': regs[x] += 1
            case 'dec': regs[x] -= 1

        i += int(y) if instr == 'jnz' and eval(x) else 1

    return regs['a']


print(run(Is), run(Is, 1))
