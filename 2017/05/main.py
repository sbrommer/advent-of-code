def get_steps(jumps, part2=False):
    steps = 0
    i = 0

    while 0 <= i < len(jumps):
        temp = i + jumps[i]
        jumps[i] += -1 if part2 and jumps[i] >= 3 else 1
        i = temp
        steps += 1

    return steps


jumps = [int(n) for n in open(0).readlines()]

print(get_steps(jumps.copy()), get_steps(jumps, True))
