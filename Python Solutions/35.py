'''
The number, 197, is called a circular prime because all rotations of the digits:
197, 971, and 719, are themselves prime.
There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
How many circular primes are there below one million?
'''

def isPrime(n):
    if n == 2 or n == 3:
        return True

    for i in range(2, int(n**0.5) + 3):
        if n % i == 0:
            return False
    return True


def getPermutations(n):
    '''
    Appends all permutations of the list n to permute_lst
    '''
    lst = []
    lst.append(int("".join(n)))
    for i in range(len(n)-1):
        n = n[1:] + [n[0]]
        if int("".join(n)) not in lst:
            lst.append(int("".join(n)))

    return lst


def toList(n):
    l = []
    for digit in str(n):
        l.append(digit)
    return l


circular_primes = [2, 3, 5]
prime_list = []
for i in range(2, 1000001):
    if isPrime(i):
        prime_list.append(i)


for i in prime_list:
    if i in circular_primes:
        print(i, "is a circular prime")
    elif '0' not in str(i) and '2' not in str(i) and '4' not in str(i) and '5' not in str(i) and '6' not in str(i) and '8' not in str(i):
        permute_lst = getPermutations(toList(i))
        circle_prime = True
        for num in permute_lst:
            if num not in prime_list:
                circle_prime = False
                break

        if circle_prime:
            print(i, "is a circular prime")
            for num in permute_lst:
                circular_primes.append(int(num))

print(len(circular_primes))
