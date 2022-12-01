elves = open(0).read().split('\n\n')
elves = [sum(map(int, elf.split())) for elf in elves]
elves.sort(reverse=True)
print(elves[0], sum(elves[:3]))
