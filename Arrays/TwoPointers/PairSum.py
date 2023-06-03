"""
Find if pair sum = K .
    A[i] + A[j] = K (Given)
Given N distinct elements in a sorted array
Difficulty Level : Easy
"""

def check_pair_sorted(A,K):
    n = len(A)
    p1 = 0
    p2 = n-1

    while p1 < p2:
        if A[p1] + A[p2] == K:
            return True
        elif A[p1] + A[p2] < K:
            p1 += 1
        else:
            p2 -= 1

    return False
A1 = [3,7,8,12,19]
K1 = 15
A2 =[2,5,8,11,15]
K2 = 16
print("Input" , A1,"K ",K1)
print(check_pair_sorted(A1,K1))
print("Input" , A2,"K ",K2)
print(check_pair_sorted(A2,K2))
