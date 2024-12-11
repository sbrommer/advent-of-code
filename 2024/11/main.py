from math import log10
from functools import cache


@cache
def blink(n, s):
    def blink_(s): return blink(n-1, s)
    
    if n == 0: return 1
    if s == 0: return blink_(1)

    d = 1+int(log10(s)) if s else 0
    if d % 2: return blink_(s*2024)

    u, v = divmod(s, 10**(d//2))
    return blink_(u) + blink_(v)


stones = [*map(int, input().split())]

print(*[sum(blink(n, s) for s in stones) for n in [25, 75]])
