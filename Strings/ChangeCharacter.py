"""
====================
Problem Description
====================
You are given a string A of size N consisting of lowercase alphabets.
You can change at most B characters in the given string to any other
lowercase alphabet such that the number of distinct characters in the string is minimized.
Find the minimum number of distinct characters in the resulting string.

====================
Problem Constraints
====================
1 <= N <= 100000
0 <= B < N

====================
Input Format
====================
The first argument is a string A.
The second argument is an integer B.

====================
Output Format
====================
Return an integer denoting the minimum number of distinct characters in the string.

====================
Example Input
====================
A = "abcabbccd"
B = 3

====================
Example Output
====================
2

====================
Example Explanation
====================
We can change both 'a' and one 'd' into 'b'.So the new string becomes "bbcbbbccb".
So the minimum number of distinct character will be 2.
"""
def ChangeCharacter(A, B):
    freq =[0]*26
    for char in A:
        code = ord(char) - ord('a')
        freq[code] += 1
    freq_sorted = sorted(freq)

    for i in range(26):
        if freq_sorted[i] != 0:
            if B > 0 and B >= freq_sorted[i]:
                B -= freq_sorted[i]
            else:
                return 26-i

    return 0
A = "abcabbccd"
B = 3
print(ChangeCharacter(A,B))