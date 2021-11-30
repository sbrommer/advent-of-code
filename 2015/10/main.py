from sys import stdin

x = stdin.readline().strip()

def look_and_say(n):
    count = 1
    prev = n[0]
    say = ''

    for char in n[1:]:
        if char == prev:
            count += 1
        else:
            say += str(count) + prev
            count = 1

        prev = char

    say += str(count) + prev
    return say

# Part 1
for i in range(40):
    x = look_and_say(x)
print(len(x))

# Part 2
for i in range(10):
    x = look_and_say(x)
print(len(x))
