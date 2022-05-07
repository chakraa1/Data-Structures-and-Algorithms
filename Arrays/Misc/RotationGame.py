"""
=====================
Problem Description
=====================
Given an integer array A and an integer B, you have to print the same array after rotating it B times towards the right.
NOTE: You can use extra memory.

=====================
Problem Constraints
=====================
1 <= |A| <= 106
1 <= A[i] <= 109
1 <= B <= 109

=====================
Input Format
=====================
The first line begins with an integer A denoting the length of an array, and then A integers represent the array elements.
The second line contains a single integer B

=====================
Output Format
=====================
Print an array of integers which is the Bth right rotation of input array A, on a separate line.

=====================
Example Input
=====================
Input 1:

 4 1 2 3 4
 2
Input 2:

 3 1 2 2
 3

=====================
Example Output
=====================

Output 1: 3 4 1 2
Output 2: 1 2 2

=====================
Example Explanation
=====================
Explanation 1: [1,2,3,4] => [4,1,2,3] => [3,4,1,2]
Explanation 2: [1,2,2] => [2,1,2] => [2,2,1] => [1,2,2]

"""
def RotationGame(A,B):
    n = len(A)
    B = B % n
    if B > n:
        return A
    else:
        ans = [0] * n
        j = 0
        for i in range(B,n):
            ans[i] = A[j]
            j += 1

        for i in range(B):
            ans[i] = A[n - B + i]

        return ans

A = [1,2,3,4]
B = 2
A = [1,2,2]
B = 3
print(RotationGame(A,B))