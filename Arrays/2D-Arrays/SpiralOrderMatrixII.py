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
def PrintBoundarySquareMatrixII(A):
    M=[[0]*A for _ in range(A)]
    element=1
    for icol in range(A):
        for irow in range(A):
            M[icol][irow]=element
            element +=1
    print(M)

    # Current position
    r, c = 0, 0
    direction = 'right'
    while(True):
        # print(M[r][c])
        if direction == 'right': # Moving right
            # Change direction if boundary is being hit
            if c == A-1:
                direction = 'down'
                r += 1
            else:
                c += 1
        elif direction == 'left': # Moving left
            if c == 0:
                direction = 'up'
                r -= 1
            else:
                c -= 1
        elif direction == 'down': # Moving down
            if r == A-1:
                direction = 'left'
                c -= 1
            else:
                r += 1
        elif direction == 'up':  # Moving up
            if r == 1:
                break
                # direction = 'right'
                # c += 1
            else:
                r -= 1
        #print(r,c)
    return M
def SpiralOrderSquareMatrixII(A):
    print(A)

A=1
A=2
print(PrintBoundarySquareMatrixII(A))
#print(SpiralOrderOuterSquareMatrixII(A))
