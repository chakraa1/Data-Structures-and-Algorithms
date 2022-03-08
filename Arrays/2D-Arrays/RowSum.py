def solve(self, A):
    rows = len(A)
    cols = len(A[0])
    result = []

    for irow in range(rows):
        total = 0
        for icol in range(cols):
            total += A[irow][icol]
        result.append(total)

    return result