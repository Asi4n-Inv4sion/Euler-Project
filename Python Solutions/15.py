'''
Starting in the top left corner of a 2×2 grid, and only being able to move to
the right and down, there are exactly 6 routes to the bottom right corner.
How many such routes are there through a 20×20 grid?
'''
import math

def num_paths(length, width):
    return math.factorial(length + width) / (math.factorial(length) * math.factorial(width))

print(int(num_paths(20, 20)))
