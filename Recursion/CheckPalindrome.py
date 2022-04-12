"""
======================
Problem Description
======================
Write a recursive function that checks whether string A is a palindrome or Not.
Return 1 if the string A is a palindrome, else return 0.
Note: A palindrome is a string that's the same when read forward and backward.


======================
Problem Constraints
======================
1 <= A <= 50000

String A consists only of lowercase letters.

======================
Input Format
======================
The first and only argument is a string A.

======================
Output Format
======================
Return 1 if the string A is a palindrome, else return 0.


======================
Example Input
======================
Input 1: A = "naman"
Input 2: A = "strings"

======================
Example Output
======================
Output 1: 1
Output 2: 0

======================
Example Explanation
======================
Explanation 1:

 "naman" is a palindomic string, so return 1.
Explanation 2:

 "strings" is not a palindrome, so return 0.



See Expected Output
"""
import sys
sys.setrecursionlimit(1000000)
def isPalindrome(A,s,e):
    if s == e or e - s == 1 :
        return 1
    else:
        if A[s] == A[e]:
            return isPalindrome(A,s + 1, e -1)
        else:
            return 0

def isPalindrome2(A,s,e):
    if s >= e:
        return 1
    if A[s] == A[e]:
        return isPalindrome2(A,s+1,e-1)

    return 0
def solve(A):
    if len(A) == 0:
        return 1
    return isPalindrome2(A,0,len(A)-1)

print(solve("naman"))
print(solve("abcd"))
print(solve("nitin"))