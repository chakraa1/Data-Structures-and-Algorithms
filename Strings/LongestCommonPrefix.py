"""
====================
Problem Description
====================
Given the array of strings A, you need to find the longest string S, which is the prefix of ALL the strings
in the array.The longest common prefix for a pair of strings S1 and S2 is the longest string S which is the
prefix of both S1 and S2.

Example: the longest common prefix of "abcdefgh" and "abcefgh" is "abc".

====================
Problem Constraints
====================
0 <= sum of length of all strings <= 1000000

====================
Input Format
====================
The only argument given is an array of strings A.

====================
Output Format
====================
Return the longest common prefix of all strings in A.

====================
Example Input
====================
Input 1: A = ["abcdefgh", "aefghijk", "abcefgh"]
Input 2: A = ["abab", "ab", "abcd"];

====================
Example Output
====================
Output 1: "a"
Output 2: "ab"

====================
Example Explanation
====================
Explanation 1: Longest common prefix of all the strings is "a".
Explanation 2: Longest common prefix of all the strings is "ab"
"""
def LongestCommonPrefix(A):
    n = len(A)
    if n == 0:
        return ""

    if n == 1:
        return A[0]

    min_common_len = float('inf')
    for s in A:
        min_common_len = min(len(s), min_common_len)

    B = sorted(A)

    i = 0
    while i < min_common_len and B[0][i] == B[n - 1][i]:
        i += 1

    return A[0][0:i]

A = ["abcdefgh", "aefghijk", "abcefgh"]
#A = ["abab", "ab", "abcd"]
print(LongestCommonPrefix(A))