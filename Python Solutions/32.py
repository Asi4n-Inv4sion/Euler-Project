'''
We shall say that an n-digit number is pandigital if it makes use of all the
digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through
5 pandigital.
The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing
multiplicand, multiplier, and product is 1 through 9 pandigital.
Find the sum of all products whose multiplicand/multiplier/product identity can
be written as a 1 through 9 pandigital.
HINT: Some products can be obtained in more than one way so be sure to only
include it once in your sum.
'''

def isPandigital(a:int, b:int):
    digits = []
    for digit in str(a):
        digits.append(digit)

    for digit in str(b):
        digits.append(digit)

    for digit in str(a*b):
        digits.append(digit)

    if len(digits) != 9:
        return False

    for i in range(1, 10):
        if digits.count(str(i)) != 1:
            return False

    return True

products = []
for i in range(1, 100):
    for j in range(i, 10000):
        if i*j not in products and isPandigital(i, j): # account for repeating products
            products.append(i*j)
        elif len(str(i*j)) + len(str(i)) + len(str(j)) > 9:
            break  # end inner loop if the total numbers used is greater than 9

sum = 0
for num in products:
    sum += num

print(sum)
