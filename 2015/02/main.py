from sys import stdin

paper = 0
ribbon = 0

for line in stdin.readlines():
    l, w, h = list(map(int, line.split('x')))

    paper += 2*l*w + 2*w*h + 2*h*l # area
    paper += min([l*w, w*h, h*l]) # slack

    ribbon += min([2*(l+w), 2*(w+h), 2*(h+l)]) # ribbon
    ribbon += l*w*h # bow

print(paper)
print(ribbon)
