"""
=====================
Problem Description
=====================
Shaggy has an array A consisting of N elements.
We call a pair of distinct indices in that array a special if elements at those indices in the array are equal.
Shaggy wants you to find a special pair such that the distance between that pair is minimum.
Distance between two indices is defined as |i-j|. If there is no special pair in the array, then return -1.

=====================
Problem Constraints
=====================
1 <= |A| <= 105

=====================
Input Format
=====================
The first and only argument is an integer array A.

=====================
Output Format
=====================
Return one integer corresponding to the minimum possible distance between a special pair.

=====================
Example Input
=====================
Input 1: A = [7, 1, 3, 4, 1, 7]
Input 2: A = [1, 1]

=====================
Example Output
=====================
Output 1: 3
Output 2: 1


=====================
Example Explanation
=====================
Explanation 1:

Here we have 2 options:
1. A[1] and A[4] are both 1 so (1,4) is a special pair and |1-4|=3.
2. A[0] and A[5] are both 7 so (0,5) is a special pair and |0-5|=5.
Therefore the minimum possible distance is 3.

Explanation 2: Only possibility is choosing A[1] and A[2].
"""

def ShaggyAndDistances(A):
    ans = -1
    n = len(A)

    l = 0
    r = n - 1
    min_distance = float('inf')
    while l < n and r > 0 and l < r:
        if A[l] == A[r]:
            d = r - l
            min_distance = min(d,min_distance)
        print(l,r,min_distance)
        l += 1
        r -= 1
    if min_distance > 0:
        ans = min_distance

    return ans
def ShaggyAndDistances2(A):
    ans = -1
    n = len(A)

    freq = dict()
    print(A)

    min_distance = float('inf')
    for s in range(len(A)):
        for e in range(s,n):
            if A[s] == A[e]:
                d = e - s
                min_distance = min(d, min_distance)

    if min_distance > 0:
        ans = min_distance

    return ans

A = [7, 1, 3, 4, 1, 7]
#A = [1, 1]
print(ShaggyAndDistances2(A))