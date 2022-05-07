"""
====================
Problem Description
====================
You are given an integer array A. You have to find the second largest element/value in the array or report that no such element exists.

====================
Problem Constraints
====================
1 <= |A| <= 105
0 <= A[i] <= 109

====================
Input Format
====================
The first argument is an integer array A.

====================
Output Format
====================
Return the second largest element. If no such element exist then return -1.

====================
Example Input
====================
Input 1: A = [2, 1, 2]
Input 2: A = [2]

====================
Example Output
====================
Output 1: 2
Output 2:-1

====================
Example Explanation
====================
Explanation 1:

 First largest element = 2
 Second largest element = 2
 Third largest element = 1

Explanation 2:

 There is no second largest element in the array.

"""
def SecondLargest(A):
    ans = -1

    max_v = - float('inf')
    n = len(A)
    """
    Find first max
    """
    for i in range(n):
        if A[i] > max_v:
            max_v = A[i]
    """
    Replace all first max by min value
    """
    for i in range(n):
        if A[i] == max_v:
            A[i] = - float('inf')

    """
     Again calculate max 
    """
    max_v = -float('inf')
    for i in range(n):
        if A[i] > max_v:
            ans = A[i]

    return ans

A = [2, 1, 2]
A = [2]
print(SecondLargest(A))