captcha = input()


def solve(offset):
    comparison = captcha[offset:] + captcha[:offset]

    s = 0
    for i, j in zip(captcha, comparison):
        s += (i == j) * int(i)

    return s


print(solve(1), solve(len(captcha) // 2))
