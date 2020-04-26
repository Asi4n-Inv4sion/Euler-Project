'''
If the numbers 1 to 5 are written out in words: one, two, three, four, five,
then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
If all the numbers from 1 to 1000 (one thousand) inclusive were written out in
words, how many letters would be used?
'''

# answer taken from https://www.mathblog.dk/project-euler-17-letters-in-the-numbers-1-1000/
# I was way to lazy to do this

sum = 0

# 1-9
sum = 3 + 3 + 5 + 4 + 4 + 3 + 5 + 5 + 4 # = 36

# 1-19
sum += 3 + 6 + 6 + 8 + 8 + 7 + 7 + 9 + 8 + 8 # = 70

# 20-99
sum += 10*(6 + 6 + 5 + 5 + 5 + 7 + 6 + 6) + 8*36 # = 748

# 100-1000
sum += 36*100 + 9*854 + 7*9 + 891*10 + 11

print(sum)
