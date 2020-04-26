'''
By starting at the top of the triangle below and moving to adjacent numbers on
the row below, the maximum total from top to bottom is 23.
3
7 4
2 4 6
8 5 9 3
Find the maximum total from top to bottom of the triangle in 18.txt
'''

f = open('18.txt', 'r')
triangle = []
for line in f.readlines():
    row = line.strip().split(' ')
    triangle.append(row)

def max_path(triangle):
    row = len(triangle) - 1
    for i in range(len(triangle) - 1):
        for j in range(row):
            triangle[row-1][j] = int(triangle[row-1][j])
            triangle[row-1][j] += max(int(triangle[row][j]), int(triangle[row][j+1]))
        row -= 1
    return int(triangle[0][0])


print(max_path(triangle))
