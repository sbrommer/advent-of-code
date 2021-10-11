from sys import stdin

directions = stdin.readline()

# part 1
print(directions.count('(') - directions.count(')'))

# part 2
floor = 0
for i, d in enumerate(directions):
    floor += (d == '(') - (d == ')')
    if floor < 0:
        print(i + 1)
        break
