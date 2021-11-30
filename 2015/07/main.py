from sys import stdin

# read circuit
circuit = {}
for line in stdin.readlines():
    line = line.strip()
    ops, wire = line.split(' -> ')
    ops = ops.strip().split(' ')

    circuit[wire] = ops

# evaluate
def evaluate(wire, register):
    def eval(x):
        return int(x) if x.isdigit() else evaluate(x, register)

    if wire not in register.keys():
        ops = circuit[wire]

        if len(ops) == 1:
            register[wire] = eval(ops[0])

        elif len(ops) == 2: # ops[0] == 'NOT'
            x = eval(ops[1])
            register[wire] = ~x & 0xffff

        else: # len(ops) == 3
            l = eval(ops[0])
            r = eval(ops[2])

            if ops[1] == 'AND':
                register[wire] = l & r

            elif ops[1] == 'OR':
                register[wire] = l | r

            elif ops[1] == 'LSHIFT':
                register[wire] = l << r

            else: # ops[1] == 'RSHIFT':
                register[wire] = l >> r

    return register[wire]

# Part 1
a = evaluate('a', {})
print(a)

# Part 2
circuit['b'] = [str(a)]
print(evaluate('a', {}))
