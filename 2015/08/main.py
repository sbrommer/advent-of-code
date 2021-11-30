from sys import stdin

n = 0
m = 0

line = stdin.readline().strip()
while len(line):
    n += len(line) - len(eval(line))
    m += 2 + line.count('\\') + line.count('"')
    line = stdin.readline().strip()

print(n)
print(m)
