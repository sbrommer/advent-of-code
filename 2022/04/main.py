from parse import parse

t1 = 0
t2 = 0

for line in open(0):
    s1, e1, s2, e2 = parse('{:d}-{:d},{:d}-{:d}\n', line)

    t1 += s1 <= s2 <= e2 <= e1 or s2 <= s1 <= e1 <= e2
    t2 += s1 <= s2 <= e1 or s2 <= s1 <= e2

print(t1, t2)
