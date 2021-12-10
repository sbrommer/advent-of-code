# Constants
moves = {'U': -1j, 'D': 1j, 'R': 1, 'L': -1}


# Parse
def parse_line(line):
    return list(map(moves.get, line.strip()))


lines = list(map(parse_line, open(0).readlines()))


# Helper function
def print_code(button, buttons, labels):
    for line in lines:
        for move in line:
            if button + move in set(buttons):
                button += move
        print(labels[buttons.index(button)], end='')
    print()


# Part 1
buttons = [0,  1,    2,
           1j, 1+1j, 2+1j,
           2j, 1+2j, 2+2j]

print_code(1+1j, buttons, '123456789')

# Part 2
buttons = [          2,
               1+1j, 2+1j, 3+1j,
           2j, 1+2j, 2+2j, 3+2j, 4+2j,
               1+3j, 2+3j, 3+3j,
                     2+4j]

print_code(2j, buttons, '123456789ABCD')
