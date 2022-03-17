"""
====================
Problem Description
====================
Reverse the bits of an 32 bit unsigned integer A.

====================
Problem Constraints
====================
0 <= A <= 232

====================
Input Format
====================
First and only argument of input contains an integer A.

====================
Output Format
====================
Return a single unsigned integer denoting the decimal value of reversed bits.

====================
Example Input
====================
Input 1: 0
Input 2: 3

====================
Example Output
====================
Output 1: 0
Output 2: 3221225472

====================
Example Explanation
====================
Explanation 1:

        00000000000000000000000000000000
=>      00000000000000000000000000000000
Explanation 2:

        00000000000000000000000000000011
=>      11000000000000000000000000000000

"""

def ReverseBits(A):
    ans = 0
    for i in reversed(range(32)):
        rev_index = 31-i
        if A & (1 << i): # Checking if ith bit is ON or not
            ans = ans | (1 << rev_index) # Setting ith bit with n-i th bit
    return ans
A = 3
print(ReverseBits(A))