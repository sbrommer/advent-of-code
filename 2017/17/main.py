def spinlock(steps):
    buffer, pos = [0], 0

    for i in range(1, 2018):
        pos = (pos + steps) % i
        buffer = buffer[:pos+1] + [i] + buffer[pos+1:]
        pos = (pos + 1) % (i + 1)

    return buffer[(pos + 1) % len(buffer)]


def angry_spinlock(steps):
    value, pos = -1, 0

    for i in range(1, 50_000_001):
        pos = (pos + steps) % i
        if pos == 0:
            value = i
        pos = (pos + 1) % (i + 1)

    return value


steps = int(input())

print(spinlock(steps), angry_spinlock(steps))
