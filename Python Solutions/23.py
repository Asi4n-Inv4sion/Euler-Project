'''
A perfect number is a number for which the sum of its proper divisors is exactly
equal to the number. For example, the sum of the proper divisors of 28 would be
1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.
A number n is called deficient if the sum of its proper divisors is less than n
and it is called abundant if this sum exceeds n.
As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest
number that can be written as the sum of two abundant numbers is 24.
By mathematical analysis, it can be shown that all integers greater than 28123
can be written as the sum of two abundant numbers. However, this upper limit
cannot be reduced any further by analysis even though it is known that the
greatest number that cannot be expressed as the sum of two abundant numbers is
less than this limit.
Find the sum of all the positive integers which cannot be written as the sum of
two abundant numbers.
'''

def sum_of_factors(n):
    factors = 1
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            factors += i + n//i

    if int(n**0.5) * int(n**0.5) == n:
        factors -= int(n**0.5)

    return factors


def is_abundant(n):
    return sum_of_factors(n) > n


abundant = []
for i in range(1, 28124): # remember to not include 0
    if is_abundant(i):
        abundant.append(i)

sum_of_abundant = {}

for j in abundant: # for dictionary
    for k in abundant:
        if k + j <= i:
            sum_of_abundant[k+j] = True
        else:
            break

sum = 0

for i in range(28124):
    if i not in sum_of_abundant:
        sum += i

print(sum)
