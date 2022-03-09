def matrixTranspose(A):
    result=[]
    rows=len(A)
    cols=len(A[0])

    result=[[0 for j in range(rows)] for i in range(cols)]
    for icol in range(cols):
        for irow in range(rows):
            result[icol][irow]=A[irow][icol]
    return result

def TransposeSquareInplaceUpdate(A):
    n=len(A)
    for irow in range(n):
        # Enforcing upper triangle i.e. cols >= rows
        for icol in range(irow,n):
            A[irow][icol],A[icol][irow]=A[icol][irow],A[irow][icol]
    return A
A=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrixTranspose(A))
print(TransposeSquareInplaceUpdate(A))