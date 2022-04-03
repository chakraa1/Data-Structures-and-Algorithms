"""
===================
Problem Description
===================
Given an array of integers A, find and return whether the given array contains a non-empty subarray with a sum equal to 0.
If the given array contains a sub-array with sum zero return 1, else return 0.

===================
Problem Constraints
===================
1 <= |A| <= 100000
-10^9 <= A[i] <= 10^9

===================
Input Format
===================
The only argument given is the integer array A.

===================
Output Format
===================
Return whether the given array contains a subarray with a sum equal to 0.

===================
Example Input
===================
Input 1: A = [1, 2, 3, 4, 5]
Input 2: A = [-1, 1]

===================
Example Output
===================
Output 1: 0
Output 2: 1

===================
Example Explanation
===================
Explanation 1: No subarray has sum 0.
Explanation 2: The array has sum 0.

"""
def SubArrayWithZeroSum(A):
    ans = 0
    seen = set()
    prefix_sum = 0
    for x in A:
        if x == 0:
            return 1
        prefix_sum += x
        if prefix_sum == 0 or prefix_sum in seen:
            return 1
        seen.add(prefix_sum)
    return ans

A = [1, 2, 3, 4, 5]
A = [-1, 1]
print(SubArrayWithZeroSum(A))