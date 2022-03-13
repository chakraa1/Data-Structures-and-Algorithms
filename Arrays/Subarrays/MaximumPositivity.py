"""
===================
Problem Description
===================
Given an array of integers A, of size N.
Return the maximum size subarray of A having only non-negative elements.
If there are more than one such subarray, return the one having the smallest starting index in A.
NOTE: It is guaranteed that an answer always exists.

===================
Problem Constraints
===================
1 <= N <= 105
-109 <= A[i] <= 109

===================
Input Format
===================
The first and only argument given is the integer array A.

===================
Output Format
===================
Return maximum size subarray of A having only non-negative elements.
If there are more than one such subarrays, return the one having earliest starting index in A.

===================
Example Input
===================
Input 1: A = [5, 6, -1, 7, 8]
Input 2: A = [1, 2, 3, 4, 5, 6]

===================
Example Output
===================
Output 1: [5, 6]
Output 2: [1, 2, 3, 4, 5, 6]

===================
Example Explanation
===================
Explanation 1:

 There are two subarrays of size 2 having only non-negative elements.
 1. [5, 6]  starting point  = 0
 2. [7, 8]  starting point  = 3
 As starting point of 1 is smaller, return [5, 6]
Explanation 2:

 There is only one subarray of size 6 having only non-negative elements:
 [1, 2, 3, 4, 5, 6]

"""

def MaximumPositivity(A):
    max_subarray_length = 0
    N = len(A)

    min_start = -1
    min_end = -1

    for start in range(N):
        for end in range(start,N):
            isPositive = True
            for i in range(start,end+1):
                if A[i] < 0:
                    isPositive = False
                    break
            current_subarray_length = end - start + 1
            if isPositive and (current_subarray_length > max_subarray_length):
                max_subarray_length=current_subarray_length
                min_start = start
                min_end = end

    return A[min_start:min_end+1]

# A = [5, 6, -1, 7, 8]
A = [1, 2, 3, 4, 5, 6]
print(MaximumPositivity(A))