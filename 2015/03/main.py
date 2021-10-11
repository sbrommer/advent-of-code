from sys import stdin

directions = stdin.readline()

def get_houses(directions):
    x, y = 0, 0
    houses = set([(x, y)])

    for direction in directions:
        if direction == '<':
            x -= 1
        elif direction == '>':
            x += 1
        elif direction == '^':
            y += 1
        elif direction == 'v':
            y -= 1

        houses.add((x, y))

    return(houses)

# part 1
print(len(get_houses(directions)))

# part 2
santa = get_houses(directions[::2])
robot = get_houses(directions[1::2])
print(len(santa.union(robot)))
