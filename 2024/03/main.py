import re


def parse(text=open(0).read()):
    m = r"mul\((\d+),(\d+)\)|(don't\(\))|(do\(\))"
    return re.findall(m, text)


def solve(memory, part1=True):
    total = 0
    enabled = True
    for n, m, dont, do in memory:
        if dont:
            enabled = part1
        elif do:
            enabled = True
        else:
            total += enabled * int(n) * int(m)
    return total


memory = parse()
print(solve(memory), solve(memory, False))
