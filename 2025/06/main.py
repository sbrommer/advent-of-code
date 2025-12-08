cat = ''.join

*inp, ops = open(0)
nrs = [*zip(*map(str.split, inp))]

print(sum(eval(f.join(nrs)) for f, nrs in zip(ops.split(), nrs)))

nrs = [cat(n).strip() for n in zip(*inp)][:-1]

problem = ''
f = ''

for op, n in zip(ops, nrs):
    if not n:
        problem += '+'
    else:
        if op != ' ':
            f = op
        if op == '*':
            problem += '1'
        problem += f + n

print(eval(problem))
