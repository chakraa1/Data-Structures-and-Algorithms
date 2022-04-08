"""
===================
Problem Description
===================
Surprisingly, in an alien language, they also use English lowercase letters, but possibly in a different order.
The order of the alphabet is some permutation of lowercase letters.
Given an array of words A of size N written in the alien language, and the order of the alphabet denoted
by string B of size 26, return 1 if and only if the given words are sorted lexicographically in this alien language
else, return 0.


===================
Problem Constraints
===================
1 <= N, length of each word <= 105

Sum of the length of all words <= 2 * 106

===================
Input Format
===================
The first argument is a string array A of size N.
The second argument is a string B of size 26, denoting the order.

===================
Output Format
===================
Return 1 if and only if the given words are sorted lexicographically in this alien language else, return 0.

===================
Example Input
===================
Input 1:

 A = ["hello", "scaler", "interviewbit"]
 B = "adhbcfegskjlponmirqtxwuvzy"

Input 2:

 A = ["fine", "none", "no"]
 B = "qwertyuiopasdfghjklzxcvbnm"

===================
Example Output
===================
Output 1: 1
Output 2: 0

===================
Example Explanation
===================
Explanation 1: The order shown in string B is: h < s < i for the given words. So return 1.
Explanation 2: "none" should be present after "no". Return 0.
"""
"""
from functools import cmp_to_key
def custom_comparator(s1,s2):
    for a,b in zip(s1,s2):
        if rank_map[a] < rank_map[b]:
            return 1
        elif rank_map[a] > rank_map[b]:
            return 0
        else:
            continue

    if len(s1) < len(s2):
        return -1
    elif len(s1) > len(s2):
        return 1
    else:
        return 0

def IsDictionaryCustomComparatorApproach(A,B):
    global rank_map
    rank_map = dict()
    i = 1
    for char in B:
        rank_map[char] = i
        i += 1
    A_sorted = sorted(A,key=cmp_to_key(custom_comparator))
    for i in range(len(A)):
        if A[i] != A_sorted[i]:
            return 0

    return 1
"""
def IsDictionary(A,B):
    char_rank_map = dict()
    i = 1
    for char in B:
        char_rank_map[char] = i
        i += 1

    n = len(A)

    for i in range(1,n):
        word_1 = A[i-1]
        word_2 = A[i]
        common_len = min(len(word_1), len(word_2))
        flag = False
        for j in range(common_len):
            if word_1[j] != word_2[j]:
                # Checking first not matching char
                if char_rank_map[word_1[j]] > char_rank_map[word_2[j]]:
                    # Checking Rank of first not matching char
                    return 0
                else:
                    flag = True
                    break
        # No mismatch , then we're comparing as per length
        if flag == False and len(word_1) > len(word_2):
            return 0
    return 1

A = ["hello", "scaler", "interviewbit"]

B = "adhbcfegskjlponmirqtxwuvzy"
"""
A = ["fine", "none", "no"]
B = "qwertyuiopasdfghjklzxcvbnm"

"""


print(IsDictionary(A,B))
#print(IsDictionaryCustomComparatorApproach(A,B))
#print(approach3(A,B))