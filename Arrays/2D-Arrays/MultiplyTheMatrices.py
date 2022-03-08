def solve(A, B):
    rows = len(A)
    cols = len(B[0])
    common_col_rows = len(A[0])

    result = [[0 for j in range(cols)] for i in range(rows)]

    for irow in range(rows):
        for icol in range(cols):
            for irowcol in range(common_col_rows):
                result[irow][icol] += A[irow][irowcol] * B[irowcol][icol]

    return result