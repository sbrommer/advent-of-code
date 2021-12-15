# Imports
import re

# Get input
data = input()


# Helper functions
def evaluate(data, recurse=True):
    # End condition of recursion
    if '(' not in data:
        return len(data)

    # Parse; regex finds 'left(nxr)right'
    left, n, r, right = re.findall(r'(\w*)\((\d+)x(\d+)\)(.*)', data)[0]
    n = int(n)
    r = int(r)

    # Calculate and recurse
    left = len(left)
    children = evaluate(right[:n]) if recurse else len(right[:n])
    right = evaluate(right[n:], recurse)

    return left + r * children + right


# Part 1
print(evaluate(data, recurse=False))

# Part 2
print(evaluate(data))
