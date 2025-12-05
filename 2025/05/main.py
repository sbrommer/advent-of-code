limits, available = open(0).read().strip().split('\n\n')

limits = [[int(n) for n in l.split('-')] for l in limits.split('\n')]
available = [int(n) for n in available.split('\n')]

ans1 = sum(any(l <= i <= h for l, h in limits) for i in available)

limits = sorted(limits)
ans2, p = 0, 0

for l, h in limits:
    l = max(l, p)
    ans2 += max(h-l+1, 0)
    p = h+1

print(ans1, ans2)
