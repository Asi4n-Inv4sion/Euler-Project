'''
The fraction 49/98 is a curious fraction, as an inexperienced mathematician
in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.
We shall consider fractions like, 30/50 = 3/5, to be trivial examples.
There are exactly four non-trivial examples of this type of fraction, less than
one in value, and containing two digits in the numerator and denominator.
If the product of these four fractions is given in its lowest common terms, find
the value of the denominator.
'''

numerator = 1
denominator = 1
for numer in range(10, 100):
    for denom in range(numer + 1, 100):
        for digit in range(1, 10):
            if str(digit) in str(numer) and str(digit) in str(denom):
                new_n = str(numer).replace(str(digit), '')
                new_d = str(denom).replace(str(digit), '')

                if new_n != '' and new_d != '' and new_d != '0' and int(new_n) / int(new_d) == int(numer) / int(denom):
                    numerator *= int(new_n)
                    denominator *= int(new_d)

print(numerator, '/', denominator)
# 8 / 800, the final answer for the denominator in reduced form is 100
