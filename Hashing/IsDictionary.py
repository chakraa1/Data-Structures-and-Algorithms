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
def isSorted(word_1,word_2,rank_map):
    common_len = min(len(word_1), len(word_1))
    for j in range(common_len):
        if word_1[j] != word_2[j]:
            print("Not equal check ", word_1[j], word_2[j])
            if rank_map[word_1[j]] < rank_map[word_2[j]]:
                print("rank check ", word_1[j], word_2[j], rank_map[word_1[j]], rank_map[word_2[j]])
                return False
            else:
                return True

    return len(word_1) <= len(word_2)

def IsDictionary(A,B):
    char_rank_map = dict()
    i = 1
    for char in B:
        char_rank_map[char] = i
        i += 1

    n = len(A)

    for i in range(1,n):
        if isSorted(A[i-1],A[i],char_rank_map) == False:
            return 0
        else:
            return 1

    return 1


A = ["hello", "scaler", "interviewbit"]

B = "adhbcfegskjlponmirqtxwuvzy"
"""
A = ["fine", "none", "no"]
B = "qwertyuiopasdfghjklzxcvbnm"
"""


print(IsDictionary(A,B))