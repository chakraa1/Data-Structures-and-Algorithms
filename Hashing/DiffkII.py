"""
Given an array A of integers and another non negative integer k, find if there exists 2 indices i and j such
that A[i] - A[j] = k, i != j.

Example :

Input :

A : [1 5 3]
k : 2
Output :

1
as 3 - 1 = 2

Return 0 / 1 for this problem.

"""
def diffPossible(A, B):
    present = dict()
    for i in range(len(A)):
        if B + A[i] in present:
            j = present[B + A[i]]
            if i != j:
                return 1
        elif A[i]-B in present:
            j = present[A[i]-B]
            if i != j:
                return 1
        present[A[i]] = i

    return 0
A = [1,5,3]
B = 2
print(diffPossible(A, B))
