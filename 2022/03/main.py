# Returns the priority of a single item.
def priority(x):
    return 26 * x.isupper() + ord(x.lower()) - ord('a') + 1


# Returns the priority of a list. That is, the priority of
# the one item that all lists have in common.
def priority_list(xs):
    x = next(iter(set.intersection(*map(set, xs))))
    return priority(x)


# Returns the sum of the priorities of all the sublists.
def priorities(xxs):
    return sum(map(priority_list, xxs))


rucksacks = [rucksack.strip() for rucksack in open(0)]

# Part 1
compartments = [[r[:len(r) // 2], r[len(r) // 2:]] for r in rucksacks]

print(priorities(compartments))

# Part 2
groups = [rucksacks[i:i+3] for i in range(0, len(list(rucksacks)), 3)]

print(priorities(groups))
