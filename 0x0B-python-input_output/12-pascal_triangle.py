#!/usr/bin/python3
'''A function def pascal_triangle(n): that returns
a list of lists of integers representing the Pascal’s
triangle of n: '''


def pascal_triangle(n):
    '''Print a pasacal triangle'''

    if n <= 0:
        return []

    triangle = [[0 for x in range(i + 1)] for i in range(n)]
    triangle[0] = [1]

    for row in range(1, n):
        triangle[row][0] = 1
        for j in range(1, row + 1):
            if j < len(triangle[row - 1]):
                triangle[row][j] = triangle[row -
                                            1][j - 1] + triangle[row - 1][j]
            else:
                triangle[row][j] = triangle[row - 1][0]
    return triangle
