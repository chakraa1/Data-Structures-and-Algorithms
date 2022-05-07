def ReverseArray(A):
    A = list(map(int,A.split()))
    N, A = A[0],list(A[1:])
    for i in range(N//2):
        A[i],A[N-1] = A[N-1], A[i]
        N -= 1
    print(A)
A = "5 1 2 3 4 5"
print(ReverseArray(A))
