file = open(0).read().strip()

literals = file.split('\n')

print(sum(len(l) - len(eval(l)) for l in literals),
      2 * len(literals) + file.count('\\') + file.count('"'))
