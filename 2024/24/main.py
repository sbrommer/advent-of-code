from operator import and_ as AND, or_ as OR, xor as XOR

cat = ','.join

# Parse
inp = [*map(str.strip, open(0))]

for line in inp:
    if ':' in line:
        exec(line.replace(':', '= lambda: '))

    if '->' in line:
        x, op, y, _, r = line.split()
        exec(f'def {r}(): return {op}({x}(), {y}())')


# Part 1
zs = [eval(f'z{i:02d}()') for i in range(46)]
bin = int(''.join(map(str, zs[::-1])), 2)


# Part 2
gates = [line for line in inp if '->' in line]
antes = [g[-3:] for g in gates]
swaps = [('z14', 'hbk'), ('kvn', 'z18'), ('dbb', 'z23'), ('tfn', 'cvh')]

for a, b in swaps + [s[::-1] for s in swaps]:
    i = antes.index(a)
    gates[i] = gates[i][:-3] + b


def find(op, x, y, z=None):
    z = z if z else ''

    gate = [g for g in gates if
            g.startswith(f'{x} {op} {y} -> {z}') or
            g.startswith(f'{y} {op} {x} -> {z}')]

    if not gate:
        e = f'Could not find {x} {op} {y} -> {z}'
        raise Exception(e)

    return gate[0].split()[-1]


def adder(x, y, z, co, z2=None):
    t1 = find('XOR', x, y)
    z  = find('XOR', t1, co, z)
    t2 = find('AND', x, y)
    t3 = find('AND', co, t1)
    co = find('OR', t2, t3, z2)
    return co


find('XOR', 'x00', 'y00', 'z00')
find('XOR', 'x00', 'y00', 'z00')
co = find('AND', 'x00', 'y00')

for i in range(1, 45):
    n = f'{i:02}'
    x, y, z = f'x{n}', f'y{n}', f'z{n}'
    co = adder(x, y, z, co, 'z45' if i == 44 else None)


# Answers
swaps = cat(sorted(a for s in swaps for a in s))
print(bin, swaps)
