results = list(map(int, open(0).readline().split(',')))
s = [results.count(i) for i in range(9)]

for _ in range(256):
    s = s[1:] + [s[0]]
    s[6] += s[-1]

print(sum(s))
