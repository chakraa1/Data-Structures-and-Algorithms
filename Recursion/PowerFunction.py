"""
========================
Problem Description
========================
Implement pow(A, B) % C.
In other words, given A, B and C, Find (AB % C).

Note: The remainders on division cannot be negative. In other words, make sure the answer you return is non-negative.


========================
Problem Constraints
========================
-109 <= A <= 109
0 <= B <= 109
1 <= C <= 109

========================
Input Format
========================
Given three integers A, B, C.

========================
Output Format
========================
Return an integer.

========================
Example Input
========================
A = 2, B = 3, C = 3

========================
Example Output
========================
2

========================
Example Explanation
========================
23 % 3 = 8 % 3 = 2

"""


def pow(A, B, C):
    if B == 1:
        return A % C

    if B == 0:
        return 1 % C

    half_power = pow(A, B // 2, C)

    if B % 2 == 0:
        return ((half_power % C) * (half_power % C)) % C
    else:
        return ((A % C) * (half_power % C) * (half_power % C)) % C
A = 2
B = 3
C = 3
print(pow(A,B,C))