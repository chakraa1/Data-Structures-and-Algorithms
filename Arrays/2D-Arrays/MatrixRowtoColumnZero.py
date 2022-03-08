def matrixRow2ColZero(A):
    rows = len(A)
    cols = len(A[0])

    zero_rows = []
    zero_cols = []

    for irow in range(rows):
        for icol in range(cols):
            if A[irow][icol] == 0:
                zero_rows.append(irow)
                zero_cols.append(icol)
    print(zero_rows,zero_cols)
    for irow in zero_rows:
        for icol in range(cols):
            A[irow][icol] = 0
    print(A)
    for icol in zero_cols:
        for irow in range(rows):
            A[irow][icol] = 0

    return A
A=[[1, 2, 3,4], [5, 6,7,0], [9,2,0,4]]
print(*A)
print(matrixRow2ColZero(A))