"""
===================
Problem Description
===================
Given an array A of N integers.
Find the largest continuous sequence in a array which sums to zero.

===================
Problem Constraints
===================
1 <= N <= 106
-107 <= A[i] <= 107

===================
Input Format
===================
Single argument which is an integer array A.

===================
Output Format
===================
Return an array denoting the longest continuous sequence with total sum of zero.
NOTE : If there are multiple correct answers, return the sequence which occurs first in the array.

===================
Example Input
===================
A = [1,2,-2,4,-4]

===================
Example Output
===================
[2,-2,4,-4]

===================
Example Explanation
===================
[2,-2,4,-4] is the longest sequence with total sum of zero.

"""
def LargestContinuousSequenceZeroSum(A):
    ans = []

    start = -1
    end = -1
    max_len = -float('inf')
    sum_i = 0
    sum_map = dict()
    sum_map[0] = -1

    for i in range(len(A)):
        sum_i += A[i]
        if sum_i in sum_map:
            length = i - sum_map[sum_i]
            if length > max_len:
                max_len = length
                start = sum_map[sum_i]
                end = i
        else:
            sum_map[sum_i] = i

    ans = A[start + 1:end + 1]

    return ans
A = [1,2,-2,4,-4]
print(LargestContinuousSequenceZeroSum(A))