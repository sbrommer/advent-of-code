banks = [int(n) for n in input().split()]
states = []

while tuple(banks) not in states:
    states += [tuple(banks)]
    m = max(banks)
    i = banks.index(m)
    banks[i] -= m
    for di in range(m):
        banks[(i + di + 1) % len(banks)] += 1

print(len(states), len(states) - states.index(tuple(banks)))
