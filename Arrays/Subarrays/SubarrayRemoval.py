"""
You're given an array A[N] of integers. You've to find the length of smallest sub array that can be removed
from array so that after removal , absolute value of each pair of adjacent is always B apart and
abs (A[i] - A[i+1]) <= B
"""

def subarray_removal(A,B):
    ans = 0
    n = len(A)
    flag = True
    for i in range(1,n):
        abs_diff = abs(A[i] - A[i-1])
        if abs_diff > B:
            flag = False

    if flag == True:
        return 0

    for i in range(1, n):
        abs_diff = abs(A[i] - A[i - 1])
        if abs_diff < B:
            flag = False

    if flag == True:
        return n-1
    


    return ans
A = [7,3,1]
B = 3

A = [5,10,15,20]
B = 4

A = [2,4,1,3,1]
B = 5
print(subarray_removal(A,B))