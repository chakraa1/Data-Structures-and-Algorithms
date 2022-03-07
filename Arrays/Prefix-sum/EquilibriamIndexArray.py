def EquilibriumIndexArray(A):
    total=0
    for item in A:
        total+=item
    n=len(A)
    for i in range(n):
        left=A[i-1]
        right=(total-left-A[i])
        if left == right :
            return i-1
    return -1
A=[-7, 1, 5, 2, -4, 3, 0]
print(EquilibriumIndexArray(A))