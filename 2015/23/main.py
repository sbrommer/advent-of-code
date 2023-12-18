from re import findall


def parse_line(line):
    instr, args = findall(r'(\w+) (.*)', line)[0]
    args = args.split(', ')

    return instr, args


program = [*map(parse_line, open(0))]


def run(register):
    i = 0
    while 0 <= i < len(program):
        instr, args = program[i]

        offset = 1

        match instr:
            case 'hlf':
                register[args[0]] //= 2

            case 'tpl':
                register[args[0]] *= 3

            case 'inc':
                register[args[0]] += 1

            case 'jmp':
                offset = int(args[0])

            case 'jie':
                if not register[args[0]] % 2:
                    offset = int(args[1])

            case 'jio':
                if register[args[0]] == 1:
                    offset = int(args[1])

        i += offset

    return register


# Part 1
print(*[run(register)['b']
        for register in [{'a': 0, 'b': 0}, {'a': 1, 'b': 0}]])
