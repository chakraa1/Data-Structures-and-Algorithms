"""
======================
Problem Description
======================
Given a column title as appears in an Excel sheet, return its corresponding column number.

======================
Problem Constraints
======================
1 <= length of the column title <= 5

======================
Input Format
======================
The only argument is a string that represents the column title in the excel sheet.

======================
Output Format
======================
Return a single integer that represents the corresponding column number.

======================
Example Input
======================
Input 1: AB
Input 2: ABCD

======================
Example Output
======================
Output 1: 28
Output 2: 19010

======================
Example Explanation
======================
Explanation 1:

 A -> 1
 B -> 2
 C -> 3
 ...
 Z -> 26
 AA -> 27
 AB -> 28


"""
def ExcelColumnNumber(A):
    ans = 0
    n = len(A)
    for i in range(n):
        ans *= 26
        ans += ord(A[i]) - ord('A') + 1
    return ans
A="AB"
A="ABCD"
print(ExcelColumnNumber(A))