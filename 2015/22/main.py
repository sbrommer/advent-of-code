from parse import search
from sys import maxsize

hp, dmg = search('Hit points: {:d}\nDamage: {:d}', open(0).read())


def fight(hp_me=50, hp_boss=hp, mana=500, magic_missile=0, drain=0, shield=0, poison=0, recharge=0, spent=0, my_turn=True, hard=False):
    global least_spent
    armour = 0

    # Difficulty hard
    if my_turn and hard:
        hp_me -= 1
        if hp_me <= 0:
            return

    # Do magic
    if magic_missile:
        hp_boss -= 4
        magic_missile -= 1

    if drain:
        hp_boss -= 2
        hp_me += 2
        drain -= 1

    if shield:
        armour = 7
        shield -= 1

    if poison:
        hp_boss -= 3
        poison -= 1

    if recharge:
        mana += 101
        recharge -= 1

    # Check end conditions
    if hp_boss <= 0:
        least_spent = min(least_spent, spent)
        return

    if spent > least_spent:
        return

    # Play turn
    if my_turn:
        # Try magic missile
        if 53 <= mana:
            fight(hp_me, hp_boss, mana - 53, 1, drain, shield, poison, recharge, spent + 53, not my_turn, hard)

        # Try drain
        if 73 <= mana:
            fight(hp_me, hp_boss, mana - 73, magic_missile, 1, shield, poison, recharge, spent + 73, not my_turn, hard)

        # Try shield
        if 113 <= mana and not shield:
            fight(hp_me, hp_boss, mana - 113, magic_missile, drain, 6, poison, recharge, spent + 113, not my_turn, hard)

        # Try poison
        if 173 <= mana and not poison:
            fight(hp_me, hp_boss, mana - 173, magic_missile, drain, shield, 6, recharge, spent + 173, not my_turn, hard)

        # Try recharge
        if 229 <= mana and not recharge:
            fight(hp_me, hp_boss, mana - 229, magic_missile, drain, shield, poison, 5, spent + 229, not my_turn, hard)

    else:  # boss_turn
        hp_me -= max(1, dmg - armour)
        if hp_me > 0:
            fight(hp_me, hp_boss, mana, magic_missile, drain, shield, poison, recharge, spent, not my_turn, hard)


least_spent = maxsize
fight()
print(least_spent)


least_spent = maxsize
fight(hard=True)
print(least_spent)
