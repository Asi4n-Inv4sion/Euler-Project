'''
Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.
The numbers are in 13.txt
'''

f = open('13.txt','r')
sum = 0
for line in f.readlines():
    sum += int(line.strip())

print(str(sum)[:10])
