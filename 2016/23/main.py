from math import factorial

Is = [line.split() for line in open(0)]


def run(a):
    regs = {r: 0 for r in 'abcd'}
    regs['a'] = a

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
            case 'cpy':
                if y in regs:
                    regs[y] = eval(x)
            case 'inc': regs[x] += 1
            case 'dec': regs[x] -= 1
            case 'tgl':
                i_ = i + eval(x)
                if 0 <= i_ < len(Is):
                    Is[i_] = toggle(Is[i_])

        i += eval(y) if instr == 'jnz' and eval(x) else 1

    return regs['a']


def toggle(I):
    instr, *args = I

    match instr:
        case 'cpy': return ['jnz'] + args
        case 'inc': return ['dec'] + args
        case 'dec': return ['inc'] + args
        case 'jnz': return ['cpy'] + args
        case 'tgl': return ['inc'] + args


print(run(7), factorial(12) + int(Is[19][1][0]) * int(Is[20][1][0]))
