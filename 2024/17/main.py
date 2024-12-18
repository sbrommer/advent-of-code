from re import findall

cat = ''.join

A, B, C, *program = map(int, findall(r'\d+', open(0).read()))


def run(A, B=0, C=0, program=program):
    i, out = 0, []
    while i < len(program):
        D = [0, 1, 2, 3, A, B, C]

        opcode, operand = program[i:i+2]

        match opcode:
            case 0:
                A >>= D[operand]
            case 1:
                B ^= operand
            case 2:
                B = D[operand] & 7
            case 3:
                pass
            case 4:
                B ^= C
            case 5:
                out += [D[operand] & 7]
            case 6:
                B = A >> D[operand]
            case 7:
                C = A >> D[operand]

        i = operand if opcode == 3 and A else i+2

    return out


def find(program):
    q = [0]
    for A in q:
        for A in range(A, A+8):
            r = run(A)
            if r == program:
                return A
            if r == program[-len(r):]:
                q += [A*8]


print(cat(map(str, run(A, B, C))), find(program))
