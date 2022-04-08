"""
=====================
Problem Description
=====================
Given an integer array, A of size N.
You have to find all possible non-empty subsequences of the array of numbers and then, for each subsequence,
find the difference between the largest and smallest numbers in that subsequence. Then add up all the differences
to get the number.
As the number may be large, output the number modulo 1e9 + 7 (1000000007).

NOTE: Subsequence can be non-contiguous.

=====================
Problem Constraints
=====================
1 <= N <= 10000
1<= A[i] <=1000

=====================
Input Format
=====================
First argument is an integer array A.

=====================
Output Format
=====================
Return an integer denoting the output.

=====================
Example Input
=====================
Input 1: A = [1, 2]
Input 2: A = [1]

=====================
Example Output
=====================
Output 1: 1
Output 2: 0


=====================
Example Explanation
=====================
Explanation 1:

All possible non-empty subsets are:
[1]    largest-smallest = 1 - 1 = 0
[2]    largest-smallest = 2 - 2 = 0
[1 2]  largest-smallest = 2 - 1 = 1
Sum of the differences = 0 + 0 + 1 = 1
So, the resultant number is 1

Explanation 2:

 Only 1 subsequence of 1 element is formed.

def DecimalToBinary(N):
    binary_digits = ''
    while N > 0:
        digit = N % 2
        binary_digits += ''.join(str(digit))
        N = N // 2
    return binary_digits[::-1]
def getSetBits(N):
    i = 0
    while True:
        if N & (1 << i):
            print(i)
        i += 1

        if N < (1 << i):
            break
"""
import math


def SumTheDifference(A):
    n = len(A)
    Sum = 0
    for i in range(1,2**n):
        j = 0
        min_sequence = 1001
        max_sequence = 0

        # Checking set bits of a number
        while True:
            if i & (1 << j):
                # j is set bit index
                min_sequence = min(A[j], min_sequence)
                max_sequence = max(A[j], max_sequence)
            j += 1

            if i < (1 << j):
                break

        diff = max_sequence - min_sequence
        
        Sum += diff

    return Sum

def mypower(n):
    mod = 1e9 + 7
    power = 1
    for i in range(n):
        power = (power * 2) % mod

    return power
def SumTheDifferenceOptimized(A):
    n = len(A)
    Sum = 0
    C = sorted(A)

    mod = 1e9+7
    """
    Answer is {A[N-1]2^(N-1) +A[N-2]2^(N-2) +…..+A[0]2^0} - {A[0]2^(N-1) + A[1]2^(N-2) +……+ A[0]2^0}
    A[N-1]2^(N-1) - A[0]2^(N-1)
    A[N-2]2^(N-2) - A[1]2^(N-2)
    .
    .
    .
    A[0]2^0 - A[0]2^0
    """

    for i in range(len(C)):
        diff = (mypower(n-i-1) * (C[n-i-1] - C[i]) % mod ) % mod
        Sum = (Sum + diff) % mod

    return int(Sum % mod)


A = [1, 2]
A = [1]
A = [1, 4, 3, 2, 5]
print(SumTheDifference(A))
#print( DecimalToBinary(8))
#print(GenerateSubsequence(A))
#print(getSetBits(15))
print(SumTheDifferenceOptimized(A))
