"""
===================
Problem Description
===================
On the first row, we write a 0. Now in every subsequent row, we look at the previous row and replace each
occurrence of 0 with 01, and each occurrence of 1 with 10.
Given row A and index B, return the Bth indexed symbol in row A. (The values of B are 1-indexed.) (1 indexed).

===================
Problem Constraints
===================
1 <= A <= 20
1 <= B <= 2A - 1

===================
Input Format
===================
First argument is an integer A.
Second argument is an integer B.

===================
Output Format
===================
Return an integer denoting the Bth indexed symbol in row A.

===================
Example Input
===================

===================
Input 1:
===================
 A = 2
 B = 1

===================
Input 2:
===================
 A = 2
 B = 2

===================
Example Output
===================

Output 1: 0
Output 2: 1

===================
Example Explanation
===================

Explanation 1:
===================
 Row 1: 0
 Row 2: 01

===================
Explanation 2:
===================

 Row 1: 0
 Row 2: 01

"""

def KthSymbol(A,B):
    if A == 1 and B == 1:
        return 0
    length = (2 ** (A - 1))

    if B <= length / 2:
        return KthSymbol(A-1,B)
    else:
        result = KthSymbol(A - 1, B - length/2)
        if result == 0:
            return 1
        else:
            return 0

A = 2
B = 2

print(KthSymbol(A,B))
