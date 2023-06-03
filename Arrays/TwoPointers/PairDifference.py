"""
Find if pair difference = K .
    A[j] - A[i] = K (Given)
Given N distinct elements in a sorted array
Difficulty Level : Hard
Time complexity: O(n)
Space complexity: O(1)
"""

def check_pair_difference(A,K):
    n = len(A)
    p1 = 0
    p2 = 1

    while p2 < n-1:
        if A[p2] - A[p1] == K:
            return True
        elif A[p2] - A[p1] > K:
            p1 += 1
            if p1 == p2:
                p2 += 1
        else:
            p2 += 1

    return False
A1 = [-3,0,1,3,6,8,11,14,18,25]
K1 = 5
print("Input" , A1,"K ",K1)
print(check_pair_difference(A1,K1))

