'''
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
Find the sum of all numbers which are equal to the sum of the factorial of their digits.
Note: as 1! = 1 and 2! = 2 are not sums they are not included.
'''

import math

i = 3
sum = 0

while i <= 2540160:  # found the number of digits where the max factorial sum is less than the number: 9! x 7
    num_sum = 0
    for digit in str(i):
        f = math.factorial(int(digit))
        num_sum += f

    if num_sum == i:
        sum += i

    i += 1

print(sum)
