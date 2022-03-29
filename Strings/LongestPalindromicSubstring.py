"""
=====================
Problem Description
=====================
Given a string A of size N, find and return the longest palindromic substring in A.
Substring of string A is A[i...j] where 0 <= i <= j < len(A)
Palindrome string:
A string which reads the same backwards. More formally, A is palindrome if reverse(A) = A.
Incase of conflict, return the substring which occurs first ( with the least starting index).

=====================
Problem Constraints
=====================
1 <= N <= 10000
=====================
Input Format
=====================
First and only argument is a string A.

=====================
Output Format
=====================
Return a string denoting the longest palindromic substring of string A.

=====================
Example Input
=====================
A = "aaaabaaa"

=====================
Example Output
=====================
"aaabaaa"

=====================
Example Explanation
=====================

We can see that longest palindromic substring is of length 7 and the string is "aaabaaa".
"""
def reverse_str(S):
    rev = ''
    n = len(S)
    left = 0
    right = n - 1
    while left < n:
        rev += S[right]
        left += 1
        right -= 1

    return rev

def check_palindrome(S,start,end):
    org = S[start:end + 1]
    rev = reverse_str(org)
    if rev == org:
        return org
    else:
        return ''

def longestPalindromeNSqure(A):
    n = len(A)
    if n < 2:
        return n  # if string is empty then size will be 0.
        # if n==1 then, answer will be 1(single
        # character will always palindrome)
    start = 0
    max_pal_len = 1

    for i in range(n):
        left = i - 1
        right = i + 1

        while right < n and A[right] == A[i]:
            right += 1

        while left > 0 and A[left] == A[i]:
            left -= 1

        while left > 0 and right < n and A[right] == A[left]:
            left -= 1
            right += 1

        current_pal_len = right - left + 1
        if current_pal_len > max_pal_len:
            max_pal_len = current_pal_len
            start = left + 1

    ans = A[start:start + max_pal_len]

    return ans
A = "aaaabaaa"
#A ="btootmb"
#A ="abb"

#print(reverse_str(A))
#print(check_palindrome(A))
print(longestPalindromeNSqure(A))