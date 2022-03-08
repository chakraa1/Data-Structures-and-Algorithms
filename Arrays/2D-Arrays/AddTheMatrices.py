def solve(A, B):
    rows = len(A)
    cols = len(A[0])
    result = [[0 for j in range(cols)] for i in range(rows)]
    for irow in range(rows):
        for icol in range(cols):
            result[irow][icol] = A[irow][icol] + B[irow][icol]

    return result