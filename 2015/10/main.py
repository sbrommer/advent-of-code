from itertools import groupby

x = open(0).readline().strip()

def look_and_say(n):
    return ''.join([str(len(list(g))) + c for c, g in groupby(n)])

# Part 1
for i in range(40):
    x = look_and_say(x)
print(len(x))

# Part 2
for i in range(10):
    x = look_and_say(x)
print(len(x))
