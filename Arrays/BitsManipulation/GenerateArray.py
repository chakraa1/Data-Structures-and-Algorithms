"""
Given an array A[N],
you are required to generate another array B[N], find min values of B[i] such that
A. summation of all (A[i] & B[i]) is minimum
B. All (A[i] & B[i]) > 0

===============
Input
==============
A = [2,6,9]

===============
Output
==============
B = [2,2,1]

===============
Explanation
===============
2 & 2 = 2
2 & 6 = 2
9 & 1 = 1

Min value = 2  + 2 + 1

"""

def GetArray(A):
    B = []

    n = len(A)
    for i in range(n):
        tbPosition = 0
        while(A[i] >> tbPosition) & 1 == 0:
            tbPosition += 1
        B.append(2**tbPosition)

    return B

A = [2,6,9]

print(GetArray(A))