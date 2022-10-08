from parse import search
from collections import defaultdict

bot = defaultdict(list)
output = defaultdict(list)
gives = dict()

# Parse
for line in open(0).readlines():
    init = search('value {:d} goes to bot {:d}', line)
    give = search('bot {:d} gives low to {} {:d} and high to {} {:d}', line)

    if init:
        v, b = init
        bot[b].append(v)

    if give:
        b, *give = give
        gives[b] = give

# Calculate
while bot:
    b = [b for b, v in bot.items() if len(v) == 2][0]
    values = sorted(bot[b])

    if values == [17, 61]:
        print(b)

    t0, n0, t1, n1 = gives[b]

    eval(t0)[n0].append(values[0])
    eval(t1)[n1].append(values[1])

    del bot[b]

print(output[0][0] * output[1][0] * output[2][0])
