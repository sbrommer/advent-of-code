dict1 = {('A X'): 4, ('A Y'): 8, ('A Z'): 3,
         ('B X'): 1, ('B Y'): 5, ('B Z'): 9,
         ('C X'): 7, ('C Y'): 2, ('C Z'): 6}

dict2 = {('A X'): 3, ('A Y'): 4, ('A Z'): 8,
         ('B X'): 1, ('B Y'): 5, ('B Z'): 9,
         ('C X'): 2, ('C Y'): 6, ('C Z'): 7}

lines = [line.strip() for line in open(0)]

points1 = sum(map(dict1.get, lines))
points2 = sum(map(dict2.get, lines))

print(points1, points2)
