"""
=====================
Problem Description
=====================
Given two strings A and B, find if A is a subsequence of B.
Return "YES" if A is a subsequence of B, else return "NO".

=====================
Input Format
=====================

The first argument given is the string A.
The second argument given is the string B.

=====================
Output Format
=====================
Return "YES" if A is a subsequence of B, else return "NO".
Constraints

1 <= lenght(A), length(B) <= 100000
'a' <= A[i], B[i] <= 'z'
For Example

=====================
Input 1:
=====================
    A = "bit"
    B = "dfbkjijgbbiihbmmt"

=====================
Output 1:
=====================
    YES
=====================
Input 2:
=====================
    A = "apple"
    B = "appel"
=====================
Output 2:
=====================
    "NO"


"""
def FindSubsequence(A,B):
    n = len(B)
    a_idx = 0
    b_idx = 0
    while b_idx < n:
        if A[a_idx] != B[b_idx] and a_idx < len(A):
            b_idx += 1
        else:
            a_idx += 1
            b_idx += 1

        if a_idx == len(A):
            return "YES"

    return "NO"

"""
A = "bit"
B = "dfbkjijgbbiihbmmt"



A = "zgms"
B = "mqqpuygexnhtiaghnmjutumgdsinvaocgdwnldpuvmmxojmlxwrauogirlgazgvvvvkkjuilbqoqxjvjcfboickosydxaiuqpbkiacityeckqmrvueurqdlpicqsactkknhiqtzpugdirhublskyferljekmdpcjdvwmdyqqlrpckapthyrvfaypjvupgtxigypvywiosmguoxptghvgyqjeamutlglvtzqioljzrfusuuvkgrefchbfswuqkymqxsmnftofqcngaydkxncgcjchlnnnswiosfyrzkeembnpkjhbbwosyntorwqqqrmxwnwsymbktqnbzwfjehphwfiviiygqepdmuvuywolnagtfvfwfhgrzjolistfuuvuytqcysuunfdzythwpwnlckagknxkslfiljoarxlnzsowcxoncfvpxbmnlsmfsxgoxlbsrtbmmhhekmpsiueaagpqjwmeezytkuleuirhwadrjnfugibzgicdetdikfflz"

"""
A = "apple"
B = "appel"



print(FindSubsequence(A,B))