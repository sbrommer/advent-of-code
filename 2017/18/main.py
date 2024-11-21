from collections import defaultdict, deque

# Assume the programs do not end because
# i is out of range of Is.


def parse(text=open(0)):
    return [*map(parse_line, text)]


def parse_line(line):
    label, *args = line.strip().split()
    return (label, args)


def run(Is):
    reg = defaultdict(int)
    i, f = 0, 0

    def eval(a):
        try:
            return int(a)
        except ValueError:
            return reg[a]

    while 0 <= i < len(Is):
        label, args = Is[i]
        X, Y = args[0], args[-1]

        match label:
            case 'snd': f = eval(X)
            case 'set': reg[X] = eval(Y)
            case 'add': reg[X] = eval(X) + eval(Y)
            case 'mul': reg[X] = eval(X) * eval(Y)
            case 'mod': reg[X] = eval(X) % eval(Y)
            case 'rcv':
                if eval(X):
                    return f

        i += eval(Y) if label == 'jgz' and eval(X) > 0 else 1


def program(Is, qin, qout, p):
    global count
    reg = defaultdict(int)
    reg['p'] = p
    i = 0

    def eval(a):
        try:
            return int(a)
        except ValueError:
            return reg[a]

    while 0 <= i < len(Is):
        label, args = Is[i]
        X, Y = args[0], args[-1]

        match label:
            case 'snd':
                qout.append(eval(X))
                count += p
            case 'set': reg[X] = eval(Y)
            case 'add': reg[X] = eval(X) + eval(Y)
            case 'mul': reg[X] = eval(X) * eval(Y)
            case 'mod': reg[X] = eval(X) % eval(Y)
            case 'rcv':
                while not qin:
                    yield
                else:
                    reg[X] = qin.popleft()

        i += eval(Y) if label == 'jgz' and eval(X) > 0 else 1


Is = parse()

# Part 2
count = 0
qA, qB = deque(), deque()
A, B = program(Is, qA, qB, 0), program(Is, qB, qA, 1)

next(A), next(B)
while qA or qB:
    next(A), next(B)

print(run(Is), count)
