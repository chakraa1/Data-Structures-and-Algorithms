"""
=====================
Problem Description
=====================
Given a number A. Return square root of the number if it is perfect square otherwise return -1.

=====================
Problem Constraints
=====================
1 <= A <= 108

=====================
Input Format
=====================
First argument is an integer A.

=====================
Output Format
=====================
Return an integer which is the square root of A if A is perfect square otherwise return -1.


=====================
Example Input
=====================
Input 1: A = 4
Input 2: A = 1001

=====================
Example Output
=====================
Output 1: 2
Output 2: -1

=====================
Example Explanation
=====================
Explanation 1: sqrt(4) = 2
Explanation 2: 1001 is not a perfect square.

"""
def Sqrt(A):
    i = 1
    while i < A:
        if i * i == A:
            return i
        i += 1

    return -1

def SqrtOptimized(A):
    low = 0
    high = A
    while low <= high:
        mid = (low + high) // 2
        if mid * mid > A:
            high = mid - 1
        elif mid * mid < A:
            low = mid + 1
        elif mid * mid == A:
            return mid
    return -1

A = 4
#A = 1001
A = 121
print(Sqrt(A))