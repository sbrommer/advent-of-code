def diffs(history):
    return [a - b for a, b in zip(history[1:], history)]


def extrapolate(history):
    return history[-1] + extrapolate(diffs(history)) if history else 0


lines = open(0).readlines()
report = [[*map(int, line.split())] for line in lines]

print(*[sum(extrapolate(history[::d]) for history in report) for d in [1, -1]])
