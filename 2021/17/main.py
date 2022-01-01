from parse import search

x1, x2, y1, y2 = search('target area: x={:d}..{:d}, y={:d}..{:d}',
                        open(0).readline())


# Helper functions
def triangle(n):
    return (n ** 2 + n) // 2


def hit(vx, vy, px=0, py=0):
    # Overshoot.
    if x2 < px or y1 > py:
        return False

    # Hit.
    if x1 <= px and y2 >= py:
        return True

    # Target not yet reached.
    return hit(max(vx - 1, 0), vy - 1, px + vx, py + vy)


# Part 1
print(triangle(-y1 - 1))

# Part 2
print(sum(hit(x, y) for x in range(x2+1) for y in range(y1, -y1)))
