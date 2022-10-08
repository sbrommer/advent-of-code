regs = {'a': 0, 'b': 0, 'c': 0, 'd': 0}
lines = [line.split() for line in open(0).readlines()]

i = 0

while i < len(lines):
    instr, *args = lines[i]

    if instr == 'cpy':
        v, r = args
        v = int(v) if v.isnumeric() else regs[v]
        regs[r] = v

    if instr == 'inc':
        r = args[0]
        regs[r] += 1

    if instr == 'dec':
        r = args[0]
        regs[r] -= 1

    if instr == 'jnz':
        v, n = args
        v = int(v) if v.isnumeric() else regs[v]
        n = int(n)
        if v:
            i += n - 1

    i += 1

print(regs['a'])
