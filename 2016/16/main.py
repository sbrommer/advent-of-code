from operator import eq


def process(a):
    b = ''.join(str(1 - int(i)) for i in a[::-1])
    return a + '0' + b


def checksum_helper(s):
    return list(eq(*s[i:i+2]) for i in range(0, len(s), 2))


def checksum(s):
    while not len(s := checksum_helper(s)) % 2:
        pass
    return ''.join(map(str, map(int, s)))


# l = 272
l = 35651584
state = '10010000000110000'

while len(state) < l:
    state = process(state)

state = state[:l]

print(checksum(state))
