def to_order(box):
    l, w, h = sorted(box)
    return 3*l*w + 2*l*h + 2*w*h, 2*(l+w) + l*w*h


boxes = [map(int, box.split('x')) for box in open(0)]
orders = map(to_order, boxes)

print(*map(sum, zip(*orders)))
