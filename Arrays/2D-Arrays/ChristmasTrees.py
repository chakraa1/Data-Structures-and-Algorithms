"""
=====================
Problem Description
=====================
You are given an array A consisting of heights of Christmas trees and an array B of the same size consisting of the cost of each of the trees (Bi is the cost of tree Ai, where 1 ≤ i ≤ size(A)), and you are supposed to choose 3 trees (let's say, indices p, q, and r), such that Ap < Aq < Ar, where p < q < r.
The cost of these trees is Bp + Bq + Br.

You are to choose 3 trees such that their total cost is minimum. Return that cost.
If it is not possible to choose 3 such trees return -1.

=====================
Problem Constraints
=====================

1 <= A[i], B[i] <= 109
3 <= size(A) = size(B) <= 3000

"""
def  ChristmasTrees( H, C):
    min_cost=float('inf')
    n=len(H)
    if n < 3:
        return -1

    for t_mid in range(n):
        cost_t_mid=C[t_mid]

        cost_t_left=float('inf')

        for t_left in range(t_mid):
            if H[t_left] < H[t_mid]:
                cost_t_left=min(C[t_left],cost_t_left)

        cost_t_right=float('inf')

        for t_right in range(t_mid+1,n):
            if H[t_right] > H[t_mid]:
                cost_t_right=min(C[t_right],cost_t_right)

        cost=cost_t_mid + cost_t_left + cost_t_right
        min_cost=min(min_cost,cost)

    if min_cost == float('inf'):
        return -1

    return min_cost

A = [1, 3, 5]
B = [1, 2, 3]
A = [1, 6, 4, 2, 6, 9]
B = [2, 5, 7, 3, 2, 7]
print(ChristmasTrees( A, B))
