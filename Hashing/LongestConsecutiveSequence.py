"""
====================
Problem Description
====================
Given an unsorted integer array A of size N.
Find the length of the longest set of consecutive elements from array A.

====================
Problem Constraints
====================
1 <= N <= 106
-106 <= A[i] <= 106

====================
Input Format
====================
First argument is an integer array A of size N.


====================
Output Format
====================
Return an integer denoting the length of the longest set of consecutive elements from the array A.

====================
Example Input
====================
Input 1: A = [100, 4, 200, 1, 3, 2]
Input 2: A = [2, 1]

====================
Example Output
====================
Output 1: 4
Output 2: 2

====================
Example Explanation
====================
Explanation 1: The set of consecutive elements will be [1, 2, 3, 4].
Explanation 2: The set of consecutive elements will be [1, 2].

"""
def LongestConsecutiveSequence(A):
    if len(A) == 1:
        return 1
    ans = 1
    A = sorted(A)
    prev = A[0]
    seq = set()
    for x in A[1:]:
        if x == prev + 1 or x == prev:
            if prev not in seq:
                seq.add(prev)
            seq.add(x)
            ans = max(ans, len(seq))
        else:
            seq = set()
        prev = x

    return ans
#A = [100, 4, 200, 1, 3, 2]
A = [2, 1]
print(LongestConsecutiveSequence(A))
