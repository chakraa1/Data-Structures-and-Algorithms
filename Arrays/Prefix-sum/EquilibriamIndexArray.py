"""
=====================
Problem Description
=====================
You are given an array A of integers of size N.
Your task is to find the equilibrium index of the given array
The equilibrium index of an array is an index such that the sum of elements at lower indexes is equal to the sum of elements at higher indexes.

=====================
NOTE:
=====================
Array indexing starts from 0.
If there is no equilibrium index then return -1.
If there are more than one equilibrium indexes then return the minimum index.


=====================
Problem Constraints
=====================
1 <= N <= 105
-105 <= A[i] <= 105

=====================
Input Format
=====================
First arugment is an array A .

=====================
Output Format
=====================
Return the equilibrium index of the given array. If no such index is found then return -1.

=====================
Example Input
=====================
Input 1: A=[-7, 1, 5, 2, -4, 3, 0]
Input 2: A=[1,2,3]

=====================
Example Output
=====================
Output 1: 3
Output 2: -1

=====================
Example Explanation
=====================
Explanation 1:
3 is an equilibrium index, because:
A[0] + A[1] + A[2] = A[4] + A[5] + A[6]

Explanation 2: There is no such index.

"""
def EquilibriumIndex(A):
    ans = -1
    p = [A[0]]
    for x in A[1:]:
        p.append(x + p[-1])

    print(p)

    n = len(A)
    for i in range(1,n):
        a = p[i]
        b = p[n-1] - p[i - 1]
        if a == b:
            return i

    return ans
A=[-7, 1, 5, 2, -4, 3, 0]
A=[1,2,3]
print(EquilibriumIndex(A))

def EquilibriumIndexArray(A):
    total=0
    for item in A:
        total+=item
    n=len(A)
    for i in range(n):
        left=A[i-1]
        right=(total-left-A[i])
        if left == right :
            return i-1
    return -1
A=[-7, 1, 5, 2, -4, 3, 0]
print(EquilibriumIndexArray(A))