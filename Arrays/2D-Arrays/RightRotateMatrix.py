def RightRotateMatrix(A):
    rows=len(A)
    cols=len(A[0])
    A_rotated=[[0]*cols for _ in range(rows)]

    for i in range(cols):
        for j in range(rows):
            A_rotated[j][rows-i-1] = A[i][j]

    return A_rotated
def RightRotateSquareMatrixInPlace(A):
    n=len(A)
    for i in range(n//2):
        for j in range(i,n-i-2):
            t=A[i][j]
            A[i][j]=A[n-1-i]
            A[j][n - 1 - i]=A[n-i-1][n-i-j]
            A[n-i-1][n-i-j]=A[n-j-1][i]
            A[n - j - 1][i]=t
    return A
A=[[1,2,3,4],[5,6,7,8],[9,10,11,12]]
A=[[1,2,3],[4,5,6],[7,8,9]]
#print(RightRotateMatrix(A))
print(RightRotateSquareMatrixInPlace(A))