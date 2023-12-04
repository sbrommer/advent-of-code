from collections import defaultdict

points = 0
cards = defaultdict(int)

for i, line in enumerate(open(0).readlines()):
    card = [set(nrs.split()) for nrs in line.split('|')]

    matches = len(card[0] & card[1])

    points += 2 ** matches // 2

    cards[i] += 1
    for m in range(matches):
        cards[i + m + 1] += cards[i]

print(points, sum(cards.values()))
