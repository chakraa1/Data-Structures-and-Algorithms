# Minor diagonal of a M X M matrix A is a collection of elements A[i, j] such that
# i + j = M + 1 (where i, j are 1-based)
def solve(self, A):
    rows = len(A)
    cols = len(A[0])

    ans = 0

    for irow in range(rows):
        for icol in range(cols):
            if (irow + icol == ((rows + 1) - 2)):
                ans += A[irow][icol]
    return ans