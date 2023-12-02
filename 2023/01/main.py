from re import findall


digits = {'one': 'o1e', 'two': 't2o', 'three': 't3e',
          'four': 'f4r', 'five': 'f5e', 'six': 's6x',
          'seven': 's7n', 'eight': 'e8t', 'nine': 'n9e'}


def calibrate_line(line):
    ds = findall('\d', line)
    return int(ds[0] + ds[-1]) if ds else 0


def calibrate(lines):
    return sum(map(calibrate_line, lines))


def replace_text(line):
    for d in digits.items():
        line = line.replace(*d)
    return line


lines = open(0).readlines()

print(*map(calibrate, [lines, map(replace_text, lines)]))
