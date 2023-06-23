"""
Problem statement - Count all subsets of a given set of size N
Input : N = 3
Output: 8
Explanation:
        [ ] [1] [2] [3] [1,2] [1,3] [2,3] [1,2.3]
"""

def calSubsets(N):
    if N == 0:
        return 1
    prod = calSubsets(N//2)

    if N % 2 == 0:
        return prod * prod
    else:
        return 2 * prod * prod

N = 3
print(calSubsets(N))
