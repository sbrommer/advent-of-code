from collections import defaultdict

Is = [(I[0], I[1:])
      for I in [line.strip().split()
      for line in open(0).readlines()]]

reg = defaultdict(int)


def eval(a):
    try:
        return int(a)
    except ValueError:
        return reg[a]


# Part 1
muls = 0
i = 0

while 0 <= i < len(Is):
    label, args = Is[i]
    X, Y = args[0], args[-1]

    match label:
        case 'set': reg[X] = eval(Y)
        case 'sub': reg[X] -= eval(Y)
        case 'mul':
            reg[X] *= eval(Y)
            muls += 1

    i += eval(Y) if label == 'jnz' and eval(X) != 0 else 1

print(muls)

# Part 2
reg['a'] = 1
i = 0

for _ in range(7):
    label, args = Is[i]
    X, Y = args[0], args[-1]

    match label:
        case 'set': reg[X] = eval(Y)
        case 'sub': reg[X] -= eval(Y)
        case 'mul': reg[X] *= eval(Y)

    i += eval(Y) if label == 'jnz' and eval(X) != 0 else 1

mn = reg['b']
mx = reg['c'] + 1
d = -int(Is[-2][1][1])

h = sum(any(not b % d for d in range(2, b))
        for b in range(mn, mx, d))

print(h)
