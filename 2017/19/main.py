diagram = {complex(i, j): path
           for i, line in enumerate(open(0).readlines())
           for j, path in enumerate(line)
           if path not in ' \n'}

pos = [key for key, value in diagram.items()
       if value == '|' and key.real == 0][0]

dir = 1

letters = ''
steps = 0

while pos in diagram:
    path = diagram[pos]

    if path == '+':
        dir = [dir_ for dir_ in {-1, 1, -1j, 1j} - {-dir}
               if pos+dir_ in diagram][0]

    letters += path if path not in '|-+' else ''
    steps += 1

    pos += dir

print(letters, steps)
