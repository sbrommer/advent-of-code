instructions = [[{'U': -1, 'D': 1, 'R': 1j, 'L': -1j}[i]
                for i in line.strip()] for line in open(0)]


def get_code(keypad):
    pos = [pos for pos, label in keypad.items() if label == '5'][0]

    code = ''
    for line in instructions:
        for move in line:
            if pos + move in keypad:
                pos += move
        code += keypad[pos]

    return code


keypad1 = {0: '1',   1j: '2',   2j: '3',
           1: '4', 1+1j: '5', 1+2j: '6',
           2: '7', 2+1j: '8', 2+2j: '9'}

keypad2 = {                     2j: '1',
                   1+1j: '2', 1+2j: '3', 1+3j: '4',
           2: '5', 2+1j: '6', 2+2j: '7', 2+3j: '8', 2+4j: '9',
                   3+1j: 'A', 3+2j: 'B', 3+3j: 'C',
                              4+2j: 'D'}

print(get_code(keypad1), get_code(keypad2))
