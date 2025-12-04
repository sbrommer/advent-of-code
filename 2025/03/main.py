from functools import cache

banks = [l.strip() for l in open(0).readlines()]

# # Nicer but not scalable:
# from itertools import combinations
# cat = ''.join
# print(sum(int(cat(max(combinations(b, 2)))) for b in banks))


def joltage(bank, N):
    @cache
    def helper(n=N, i=0):
        if not n:
            return 0

        if i == len(bank):
            return -10**100

        return max(helper(n-1, i+1) + int(bank[i])*10**(n-1), # include
                   helper(n,   i+1))                          # exclude
    return helper()


for n in [2, 12]:
    print(sum(joltage(b, n) for b in banks))
