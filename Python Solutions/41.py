'''
We shall say that an n-digit number is pandigital if it makes use of all the
digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?
'''

def isPrime(n):
    if n == 2:
        return True
    if n == 1:
        return False

    for i in range(2, round(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def isPandigital(n):
    counter = 0
    for num in '123456789':
        if str(n).count(num) == 1:
            counter += 1
        else:
            break

    if len(str(n)) == counter:
        return True
    else:
        return False


n = 1234
largest = 0

# only 4 digit and 7 digit pandigitals can be prime

while n <= 4321:
    skip = False
    if '0' not in str(n) and isPandigital(n) and isPrime(n):
        largest = n

    try:
        if str(n)[-3] == '0':
            n += 111
            skip = True
    except:
        pass

    if not skip:
        n += 1

n = 1234567

while n <= 7654321:
    skip = False
    if '0' not in str(n) and isPandigital(n) and isPrime(n):
        largest = n

    try:
        if str(n)[-3] == '0':
            n += 111
            skip = True
    except:
        pass

    try:
        if str(n)[-4] == '0':
            n += 1111
            skip = True
    except:
        pass

    try:
        if str(n)[-5] == '0':
            n += 11111
            skip = True
    except:
        pass

    try:
        if str(n)[-6] == '0':
            n += 111111
            skip = True
    except:
        pass

    if not skip:
        n += 1


print(largest)
