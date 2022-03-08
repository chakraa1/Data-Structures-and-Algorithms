def solve(self, A, B):
    rows = len(A)
    cols = len(A[0])
    isMatrixSame = True

    for irow in range(rows):
        for icol in range(cols):
            if A[irow][icol] != B[irow][icol]:
                isMatrixSame = False
                break

    if isMatrixSame:
        return 1
    else:
        return 0