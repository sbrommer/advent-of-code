# Imports
import numpy as np


# Helper functions
def is_triangle(sides):
    sides = sorted(sides)
    return sides[0] + sides[1] > sides[2]


def count_triangles(array):
    return sum(np.apply_along_axis(is_triangle, 1, array))


# Parse
shapes1 = np.loadtxt(open(0), int)
shapes2 = shapes1.reshape(-1, 3, 3).transpose((0, 2, 1)).reshape(-1, 3)

# Calculate
for shape in [shapes1, shapes2]:
    print(count_triangles(shape))
