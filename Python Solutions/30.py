'''
Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

1634 = 1^4 + 6^4 + 3^4 + 4^4
8208 = 8^4 + 2^4 + 0^4 + 8^4
9474 = 9^4 + 4^4 + 7^4 + 4^4
As 1 = 1^4 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
'''
# If a number as n digits, the highest sum of its fifth power digits would be n * 9^5
# To find an upperbound to search, we need to see that as n increases, the max sum decreases
# If the number of digits in the max sum is less than or equal to n, then it is an upperbound
# n = 6 shows that 6 * 9^5 = 354294 which is less than 999999, so we have an upperbound

total_sum = 0
for i in range(2, 354295):
    num = str(i)
    sum = 0
    for digit in num:
        sum += int(digit) ** 5

    if sum == i:
        total_sum += sum

print(total_sum)
