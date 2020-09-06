'''
The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1); so the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a triangle number then we shall call the word a triangle word.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common English words, how many are triangle words?
'''

def getNthTriangleNum(n):
    return 0.5 * n * (n + 1)


f = open('p042_words.txt', 'r')
words = f.readline().strip().split(',')

triangle_numbers = []

triangle_words = 0

for word in words:
    word_value = 0
    for letter in word[1:-1]:
        word_value += ord(letter) - ord('A') + 1
    if word_value not in triangle_numbers:
        if triangle_numbers == [] or triangle_numbers[-1] < word_value:
            while True:
                n = getNthTriangleNum(len(triangle_numbers) + 1)
                triangle_numbers.append(n)
                if n > word_value:
                    break
                elif n == word_value:
                    triangle_words += 1
                    break
    else:
        triangle_words += 1

print(triangle_words)
# runtime: ~0.05s
