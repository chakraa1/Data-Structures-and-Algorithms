"""
====================
Problem Description
====================
Given an array of positive integers A and an integer B, find and return first continuous subarray which adds to B.
If the answer does not exist return an array with a single element "-1".
First sub-array means the sub-array for which starting index in minimum.

====================
Problem Constraints
====================
1 <= length of the array <= 100000
1 <= A[i] <= 109
1 <= B <= 109

====================
Input Format
====================
The first argument given is the integer array A.
The second argument given is integer B.

====================
Output Format
====================
Return the first continuous sub-array which adds to B and if the answer does not exist return an array with a single element "-1".

====================
Example Input
====================
Input 1:
 A = [1, 2, 3, 4, 5]
 B = 5

Input 2:
 A = [5, 10, 20, 100, 105]
 B = 110

====================
Example Output
====================

Output 1: [2, 3]
Output 2: -1

====================
Example Explanation
====================

Explanation 1: [2, 3] sums up to 5.
Explanation 2: No subarray sums up to required number

"""
def IsGoodPair(A,K):
    present = set()
    for x in A:
        if K - x in present:
            return True
        present.add(x)

    return False

def IsSubArraySumZero(A):
    ans = False
    sum_map = dict()
    sum_1 = 0
    for i in range(len(A)):
        if A[i] == 0:
            return True
        sum_1 += A[i]
        if sum_1 == 0 or sum_1 in sum_map:
            return True
        sum_map[A[i]] = i
    return ans

def SubarrayWithGivenSum(A,B):
    ans = []
    isSumZero = IsSubArraySumZero(A)
    isGoodPair = IsGoodPair(A,B)

    if isSumZero and isGoodPair:
        return 1

    return -1

A = [1, 2, 3, 4, 5]
B = 5
"""
A = [5, 10, 20, 100, 105]
B = 110
"""

print(SubarrayWithGivenSum(A,B))
