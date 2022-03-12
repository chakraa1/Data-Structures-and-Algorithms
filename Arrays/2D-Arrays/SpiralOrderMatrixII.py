"""
Problem Description
Given an integer A, generate a square matrix filled with elements from 1 to A2 in spiral order.

Problem Constraints
1 <= A <= 1000

Input Format
First and only argument is integer A

Output Format
Return a 2-D matrix which consists of the elements in spiral order.

Example Input
Input 1:1
Input 2:2

Example Output
Output 1: [ [1] ]
Output 2: [ [1, 2], [4, 3] ]

"""
def PrintSpiralMatrixII(A):

    SP = [[0] * A for _ in range(A)]

    r, c = 0, 0
    direction = 'right'
    i = 0 # for tracking spiral interation
    counter=1
    for _ in range(A ** 2):
        SP[r][c] = counter
        counter +=1

        if direction == 'right':
            if c == A - 1 - i:
                direction = 'down'
                r += 1
            else:
                c += 1
        elif direction == 'down':
            if r == A - 1 - i:
                direction = 'left'
                c -= 1
            else:
                r += 1
        elif direction == 'up':
            if r == i + 1:
                direction = "right"
                i += 1
                c += 1
            else:
                r -= 1
        elif direction == 'left':
            if c == i:
                direction = 'up'
                r -= 1
            else:
                c -= 1
    return SP

A=1
A=5
print(PrintSpiralMatrixII(A))
