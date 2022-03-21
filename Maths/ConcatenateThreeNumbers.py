"""
====================
Problem Description
====================
Given three 2-digit integers, A, B, and C, find out the minimum number obtained by concatenating them in any order.
Return the minimum result obtained.

====================
Problem Constraints
====================
10 <= A, B, C <= 99

====================
Input Format
====================
The first argument of input contains an integer, A.
The second argument of input contains an integer, B.
The third argument of input contains an integer, C.

====================
Output Format
====================
Return an integer representing the answer.

====================
Example Input
====================
Input 1:
 A = 10
 B = 20
 C = 30

Input 2:

 A = 55
 B = 43
 C = 47

====================
Example Output
====================
Output 1: 102030
Output 2: 434755

====================
Example Explanation
====================

Explanation 1: 10 + 20 + 30 = 102030
Explanation 2: 43 + 47 + 55 = 434755

"""

def ConcatenateThreeNumbers(A,B,C):
    # sort elements
    min_elem = min(A,B,C)
    max_elem = max(A,B,C)
    mid_elem = (A + B + C) - (min_elem + max_elem)

    return min_elem * 10**4 + mid_elem * 10**2 + max_elem

A = 10
B = 20
C = 30

A = 55
B = 43
C = 47
print(ConcatenateThreeNumbers(A,B,C))