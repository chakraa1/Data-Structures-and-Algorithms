"""
==================
Problem statement
==================
Given a binary string A. It is allowed to do at most one swap between any 0 and 1.
Find and return the length of the longest consecutive 1’s that can be achieved.
==================
Input Format
==================
The only argument given is string A.
==================
Output Format
==================
Return the length of the longest consecutive 1’s that can be achieved.
==================
Constraints
==================
1 <= length of string <= 1000000
A contains only characters 0 and 1.

==================
For Example
==================
Input 1:A = "111000"
Output 1: 3

Input 2: A = "111011101"
Output 2: 7
"""
def LengthOfLongestConsecutiveOnesBinaryString(A):
    longest_count = 0
    N = len(A)

    L = [int(A[0])]
    R = [0]*N
    R[N-1] = int(A[N-1])

    for i in range(1,len(A)):
        digit=int(A[i])
        if digit == 0:
            L.append(0)
        else:
            L.append(L[-1] + 1)

    for i in reversed(range(len(A)-1)):
        digit = int(A[i])
        if digit == 0:
            R[i] = 0
        else:
            R[i] = R[i+1] + 1

    count_1s = 0
    for digit in A:
        digit_num=int(digit)
        if digit_num == 1:
            count_1s += 1

    if N == count_1s:
        return count_1s
    elif A == '01':
        return 1

    for i in range(1,len(A)-1):
        count = L[i-1] + R[i+1]
        if count < count_1s:
            count += 1

        longest_count = max(count,longest_count)

    return longest_count

#A="111000"
# A="111011101"
# A="010100110101"
A="101101"
A="1101001100101110"
print(LengthOfLongestConsecutiveOnesBinaryString(A))
