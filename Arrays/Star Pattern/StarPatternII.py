"""
=====================
Problem Description
=====================
Write a program to input an integer N from user and print hollow inverted right triangle star pattern of N lines using '*'.
See example for clarifications.

=====================
Problem Constraints
=====================
1 <= N <= 1000

=====================
Input Format
=====================
First line is an integer N
=====================
Output Format
=====================
N lines conatining only char '*' as per the question.

=====================
Example Input
=====================
Input 1: 7
Input 2: 4

=====================
Example Output
=====================
Output 1:

*******
*    *
*   *
*  *
* *
**
*
Output 2:

****
* *
**
*

"""
def StarPatternII(N):
    for row in reversed(range(1,N+1)):
        for col in range(1,row+1):
            if row == N or row == 2 or row == 1:
               print("*", end="")
            else:
                if col == 1 or col == row:
                    print("*",end="")
                else:
                    print(" ",end="")

        print()

N=7
print(StarPatternII(N))