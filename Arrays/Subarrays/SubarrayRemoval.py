"""
You're given an array A[N] of integers. You've to find the length of smallest sub array that can be removed
from array so that after removal , absolute value of each pair of adjacent is always B apart and
abs (A[i] - A[i+1]) <= B
"""

def subarray_removal(A,B):
    ans = 0
    n = len(A)
    flag = True
    # Case when diff of ALL adj elements is less than equal B
    # Hence there is no elements that we can remove , hence return 0
    for i in range(1,n):
        abs_diff = abs(A[i] - A[i-1])
        if abs_diff > B:
            flag = False

    if flag == True:
        return 0

    # Case when diff of NONE adj elements is less than equal B
    # keeping only 1 element , rest all we can remove . Hence operations
    # are N-1
    for i in range(1, n):
        abs_diff = abs(A[i] - A[i - 1])
        if abs_diff > B:
            flag = False

    if flag == True:
        return n-1
    
    # Case when diff of SOME adj elements is less than equal B
    # Cal - Pi and Si
    # If remaining array is valid or not
    # return min array length i.e. Si - Pi + 1
    Pi = 0
    Si = n - 1
    for i in range(1,n):
        if abs(A[i] - A[i -1]) <= B:
            Pi = Pi + 1
        else:
            break

    for j in range(n-2,0):
        if abs(A[j] - A[j+1]) <= B:
            Si = Si - 1
        else:
            break

    for i in range(0,Pi):
        for j in range(Si,n-1):
            l = j - i + 1
            if i != 0 and j != n - 1:
                if abs(A[i-1] - A[j + 1]) <= B:
                    ans = min(ans , l)

    return ans

A = [7,3,1]
B = 3

A = [5,10,15,20]
B = 4

A = [2,4,1,3,1]
B = 5
print(subarray_removal(A,B))