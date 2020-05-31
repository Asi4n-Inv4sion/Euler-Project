'''
The number 3797 has an interesting property. Being prime itself, it is possible
to continuously remove digits from left to right, and remain prime at each stage:
3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.
Find the sum of the only eleven primes that are both truncatable from left to right
and right to left.
NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
'''

def isPrime(n):
    if n == 2 or n == 3:
        return True
    if n == 0 or n == 1:
        return False

    for i in range(2, int(n**0.5) + 3):
        if n % i == 0:
            return False
    return True


num = 8
counter = 0
sum = 0
while counter != 11:
    trunc = False
    if isPrime(num):
        trunc = True
        for i in range(len(str(num))-1):
            if not isPrime(int(str(num)[i+1:])):
                trunc = False
            if not isPrime(int(str(num)[:i+1])):
                trunc = False

    if trunc:
        counter += 1
        sum += num
        print(num, 'is a truncatable prime')

    num += 1

print(sum)
