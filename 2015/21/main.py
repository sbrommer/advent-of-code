from parse import search
from math import ceil
import numpy as np
from itertools import product

# Shop
ws = np.array([[8, 4, 0], [10, 5, 0], [25, 6, 0], [40, 7, 0], [74, 8, 0]])
am = np.array([[0, 0, 0], [13, 0, 1], [31, 0, 2], [53, 0, 3], [75, 0, 4], [102, 0, 5]])
rs = np.array([[0, 0, 0], [25, 1, 0], [50, 2, 0], [100, 3, 0], [20, 0, 1], [40, 0, 2], [80, 0, 3]])

sets = [sum(s) for s in product(ws, am, rs, rs)
        if not all(s[2] == s[3]) or all(s[2] == rs[0,0])]

# Parse boss
hp, dmg, amr = np.array(list(search('Hit points: {:d}\nDamage: {:d}\nArmor: {:d}', open(0).read())))
Hp = 100


# Simulate fight
def i_win(Dmg, Amr):
    m = ceil(Hp / max(1, (dmg - Amr)))
    M = ceil(hp / max(1, (Dmg - amr)))
    return M <= m


# Part 1
coins = [s[0] for s in sets if i_win(*s[1:])]
print(min(coins))

# Part 2
coins = [s[0] for s in sets if not i_win(*s[1:])]
print(max(coins))
