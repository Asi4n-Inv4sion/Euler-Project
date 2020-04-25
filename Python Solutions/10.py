'''
Find the sum of all the primes below two million.
'''

def isPrime(n):
    if n == 2:
        return True

    for i in range(2, round(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

sum = 2

for i in range(3, 2000000, 2):
    if isPrime(i):
        sum += i;

print(sum)
