'''
The decimal number, 585 = 1001001001 (binary), is palindromic in both bases.
Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.
(Please note that the palindromic number, in either base, may not include leading zeros.)
'''

def isPalindrome(n:int):
    return str(n)[::-1] == str(n)

sum = 0
for i in range(1, 1000001):
    # print(i, bin(i))
    if isPalindrome(i) and isPalindrome(bin(i)[2:]):
        sum += i

print(sum)
