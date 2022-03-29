"""
====================
Problem Description
====================
Find the number of occurrences of bob in string A consisting of lowercase English alphabets.

====================
Problem Constraints
====================
1 <= |A| <= 1000

====================
Input Format
====================
The first and only argument contains the string A, consisting of lowercase English alphabets.

====================
Output Format
====================
Return an integer containing the answer.

====================
Example Input
====================
Input 1: "abobc"
Input 2: "bobob"

====================
Example Output
====================
Output 1: 1
Output 2: 2

====================
Example Explanation
====================
====================
Explanation 1:
====================
  The only occurrence is at second position.
====================
Explanation 2:
====================
Bob occures at first and third position.

"""
def CountOccurrences(A):
    cnt = 0
    prev_1 = None
    prev_2 = None
    for char in A:
        if char == 'b' and prev_1 == 'o' and prev_2 == 'b':
            cnt += 1

        prev_2 = prev_1
        prev_1 = char

    return cnt
A ="bobabtbobl"
print( CountOccurrences(A))