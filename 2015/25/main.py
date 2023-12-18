from parse import findall

r, c = findall(r'{:d}', input())
r, c = r[0], c[0]
n = sum(range(r)) + sum(range(r+1, r+c))

code = 20151125
for i in range(n):
    code *= 252533
    code %= 33554393
print(code)
