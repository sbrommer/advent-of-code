import re


# Parse
def parse_line(line):
    instr, args = re.findall(r'(\w+) (.*)', line)[0]
    args = args.split(', ')

    return (instr, args)


program = list(map(parse_line, open(0).readlines()))


# Helper function
def run():
    i = 0
    while 0 <= i < len(program):
        instr, args = program[i]

        offset = 1

        if instr == 'hlf':
            register[args[0]] //= 2

        elif instr == 'tpl':
            register[args[0]] *= 3

        elif instr == 'inc':
            register[args[0]] += 1

        elif instr == 'jmp':
            offset = int(args[0])

        elif instr == 'jie':
            if not register[args[0]] % 2:
                offset = int(args[1])

        elif instr == 'jio':
            if register[args[0]] == 1:
                offset = int(args[1])

        i += offset


# Part 1
register = {'a': 0, 'b': 0}
run()
print(register['b'])

# Part 2
register = {'a': 1, 'b': 0}
run()
print(register['b'])
