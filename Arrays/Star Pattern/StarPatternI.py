"""
===================
Problem Description
===================
Write a program to input an integer N from user and print hollow diamond star pattern series of N lines.
See example for clarifications over the pattern.

===================
Problem Constraints
===================
1 <= N <= 1000

===================
Input Format : First line is an integer N
===================

===================
Output Format
===================
N lines conatining only char '*' as per the question.

===================
Example Input
===================
Input 1: 4
Input 2: 6

===================
Example Output
===================
Output 1:

********
***  ***
**    **
*      *
*      *
**    **
***  ***
********
Output 2:

************
*****  *****
****    ****
***      ***
**        **
*          *
*          *
**        **
***      ***
****    ****
*****  *****
************
"""
def StarPatternI(N):
    for row in reversed(range(1,N+1)):
        for _ in range(1,row+1):
            print("*",end="")
        for _ in range(N-row):
            print(" ",end="")
        for _ in range(N-row):
            print(" ",end="")
        for _ in range(1,row+1):
            print("*",end="")
        print()
    for row in range(1,N+1):
        for _ in range(1,row+1):
            print("*",end="")
        for _ in range(N-row):
            print(" ",end="")
        for _ in range(N-row):
            print(" ",end="")
        for _ in range(1,row+1):
            print("*",end="")
        print()
    return 0
N=4
print(StarPatternI(N))