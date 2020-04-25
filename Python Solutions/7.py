'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10 001st prime number?
'''

def isPrime(n):
    if n == 2:
        return True

    for i in range(3, round(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


i = 3
counter = 1
while True:

    if counter == 10000 and isPrime(i):
        print("10001th prime: ", i)
        break

    elif isPrime(i):
        counter += 1

    i += 2
