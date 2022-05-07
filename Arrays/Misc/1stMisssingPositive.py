"""
===================
Problem Description
===================
Given an unsorted integer array, A of size N. Find the first missing positive integer.
Note: Your algorithm should run in O(n) time and use constant space.

===================
Problem Constraints
===================
1 <= N <= 1000000
-109 <= A[i] <= 109

===================
Input Format
===================
First argument is an integer array A.

===================
Output Format
===================
Return an integer denoting the first missing positive integer.

===================
Example Input
===================
Input 1: [1, 2, 0]
Input 2: [3, 4, -1, 1]
Input 3: [-8, -7, -6]

===================
Example Output
===================
Output 1: 3
Output 2: 2
Output 3: 1

===================
Example Explanation
===================
Explanation 1: A = [1, 2, 0]
First positive integer missing from the array is 3.

"""
def FirstMisssingPositive(A):
    ans = 0
    A = [0] + A     # Adding extra zero to make the array iterations 1 based indexing
    n = len(A)
    i = 1
    while i < n:
        if (A[i] > 0 and A[i] != i and A[i] < n) and A[i] != A[A[i]]: # ith index should have ith element assuming we're starting with zero
            A[A[i]],A[i] = A[i],A[A[i]]
        else:
            i += 1
        print(" Iterartion # --> ", i, "array ", A)

    for i in range(1,n):
        if A[i] != i:
            return i
    return n
A = [1, 2, 0]
A = [3, 4, -1, 1]
#A = [-8, -7, -6]
print(FirstMisssingPositive(A))