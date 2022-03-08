def solve(self, A):
    rows = len(A)
    cols = len(A[0])

    ans = 0

    for irow in range(rows):
        for icol in range(cols):
            if irow == icol:
                ans += A[irow][icol]

    return ans