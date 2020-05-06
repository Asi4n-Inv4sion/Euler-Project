'''
A permutation is an ordered arrangement of objects.
For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4.
If all of the permutations are listed numerically or alphabetically, we call it
lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
'''
import math

# There are 10! = 3628800 combinations
digits = [i for i in range(10)]
total = 3628800
find = 1000000
digit_permutes = []
permutation = ''
for i in range(9, -1, -1):
    j = 0
    while (j+1) * math.factorial(i) < find:
        j += 1
    digit_permutes.append(j)
    find -= j * math.factorial(i)

for i, perm in enumerate(digit_permutes):
    permutation += str(digits[perm])
    digits.pop(perm)

print(permutation)
