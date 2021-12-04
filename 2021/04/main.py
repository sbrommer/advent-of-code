import numpy as np

# Parse
balls, *cards = open(0)
cards = np.loadtxt(cards, int).reshape(-1, 5, 5)
balls = map(int, balls.split(','))

# Solve both parts
for ball in balls:
    cards[cards == ball] = -1
    marks = cards == -1
    bingos = (marks.all(1) | marks.all(2)).any(1)
    if bingos.any():
        score = sum(cards[bingos][~marks[bingos]])
        print(ball * score)
        cards = cards[~bingos]

