# Imports
from hashlib import md5

# Parse
id = open(0).readline().strip()


# Helper functions
def hash(n):
    return md5((id + str(n)).encode()).hexdigest()


# Compute
password1 = ''
password2 = ['x'] * 8

index = 0
while password2.count('x'):
    # Find pretty hashes
    h = hash(index)
    while h[:5] != '00000':
        index += 1
        h = hash(index)

    # Update password 1
    if len(password1) < 8:
        password1 += h[5]

    # Update password 2
    if h[5] in '01234567':
        i = int(h[5])
        if password2[i] == 'x':
            password2[i] = h[6]

    # Continue search
    index += 1

# Part 1
print(password1)

# Part 2
print(''.join(password2))
