"""
=====================
Problem Description
=====================
Little Ponny has been given a string A, and he wants to find out the lexicographically minimum
subsequence from it of size >= 2. Can you help him?
A string a is lexicographically smaller than string b, if the first different letter in a and b is smaller in a.
For example, "abc" is lexicographically smaller than "acc" because the first different letter is 'b' and 'c' which
is smaller in "abc".

=====================
Problem Constraints
=====================
1 <= |A| <= 105

A only contains lowercase alphabets.

=====================
Input Format
=====================
The first and the only argument of input contains the string, A.

=====================
Output Format
=====================
Return a string representing the answer.

=====================
Example Input
=====================
Input 1: A = "abcdsfhjagj"
Input 2: A = "ksdjgha"

=====================
Example Output
=====================
Output 1: "aa"
Output 2: "da"

=====================
Example Explanation
=====================

Explanation 1: "aa" is the lexicographically minimum subsequence from A.
Explanation 2: "da" is the lexicographically minimum subsequence from A

"""
def LittlePonnyAnd2Subsequence(A):
    ans = ''
    n = len(A)
    if n <= 2:
        return A

    first_min_seq_char = A[0]
    second_min_seq_char = A[1]

    for i in range(1,n):
        if i != n - 1 and A[i] < first_min_seq_char:
            first_min_seq_char = A[i]
            second_min_seq_char = 'z'
        elif A[i] < second_min_seq_char:
            second_min_seq_char = A[i]

    ans = first_min_seq_char + second_min_seq_char
    return ans

A = "abcdsfhjagj"
A = "ksdjgha"
print(LittlePonnyAnd2Subsequence(A))