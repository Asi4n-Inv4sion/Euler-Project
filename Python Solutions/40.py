'''
An irrational decimal fraction is created by concatenating the positive integers:
0.123456789101112131415161718192021...
It can be seen that the 12th digit of the fractional part is 1.
If dn represents the nth digit of the fractional part, find the value of the following expression.
d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000
'''

const = ''
i = 1
while len(const) < 1000000:
    const += str(i)
    i += 1

print(int(const[0]) * int(const[9]) * int(const[99]) * int(const[999]) *
            int(const[9999]) * int(const[99999]) * int(const[999999]))
