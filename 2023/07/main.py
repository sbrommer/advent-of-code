from collections import Counter


def parse(line):
    hand, bid = line.split()
    return hand, int(bid)


def replace_joker(hand):
    normal = hand.replace('J', '')

    replacement = max(normal, key=normal.count) if normal else 'J'
    return hand.replace('J', replacement)


def type_value(hand, joker=False):
    if joker:
        return type_value(replace_joker(hand))

    return sorted(Counter(hand).values(), reverse=True)


def cards_value(hand, joker):
    order = 'J23456789TQKA' if joker else '23456789TJQKA'
    return [order.index(c) for c in hand]


def hand_value(hand, joker):
    return type_value(hand, joker), cards_value(hand, joker)


def score(lst, joker=False):
    lst = sorted(lst, key=lambda hand_bid: hand_value(hand_bid[0], joker))
    return sum((i + 1) * b for i, (_, b) in enumerate(lst))


lst = list(map(parse, open(0).readlines()))
print(score(lst), score(lst, True))
