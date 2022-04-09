"""
====================
Problem Description
====================
You are given an array of integers A of size N.
The value of a subarray is defined as BITWISE OR of all elements in it.
Return the sum of value of all subarrays of A % 109 + 7.

====================
Problem Constraints
====================
1 <= N <= 105
1 <= A[i] <= 108

====================
Input Format
====================
The first argument given is the integer array A.

====================
Output Format
====================
Return the sum of Value of all subarrays of A % 109 + 7.


====================
Example Input
====================
Input 1: A = [1, 2, 3, 4, 5]
Input 2: A = [7, 8, 9, 10]


====================
Example Output
====================
Output 1: 71
Output 2: 110

====================
Example Explanation
====================
Explanation 1:

 Value([1]) = 1
 Value([1, 2]) = 3
 Value([1, 2, 3]) = 3
 Value([1, 2, 3, 4]) = 7
 Value([1, 2, 3, 4, 5]) = 7
 Value([2]) = 2
 Value([2, 3]) = 3
 Value([2, 3, 4]) = 7
 Value([2, 3, 4, 5]) = 7
 Value([3]) = 3
 Value([3, 4]) = 7
 Value([3, 4, 5]) = 7
 Value([4]) = 4
 Value([4, 5]) = 5
 Value([5]) = 5
 Sum of all these values = 71
 ====================
 Explanation 2:
 ====================

 Sum of value of all subarray is 110.
"""
def SubarrayOR(A):
    Sum = 0
    mod = (10 ** 9 + 7)

    prev_or_result = 0
    or_result = 0
    for i in range(len(A)):
        prev_or_result = A[i]
        for j in range(i,len(A)):
            or_result = prev_or_result | A[j]
            Sum += or_result
            prev_or_result = or_result

    return Sum % mod
def power_2(n):
    mod = (10 ** 9 + 7)
    power = 1
    for i in range(n):
        power = (power * 2) % mod

    return power
def SubarrayOROptimized(A):
    Sum = 0
    mod = (10 ** 9 + 7)
    n = len(A)
    power_2 = 1

    for i in range(28):
        last_set_bit_idx = -1
        for j in range(n):
            if A[j] & (1 << i):
                last_set_bit_idx = j
                Sum += ((j + 1) * power_2) % mod
                Sum = Sum % mod
            else:
                Sum += ((last_set_bit_idx + 1) * power_2) % mod
                Sum = Sum % mod

        power_2 = (power_2 * 2) % mod

    return int(Sum % mod)

A = [1, 2, 3, 4, 5]

#A = [7, 8, 9, 10]

print(SubarrayOROptimized(A))