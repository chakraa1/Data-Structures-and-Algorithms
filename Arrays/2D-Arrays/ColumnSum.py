def solve(A):
    rows = len(A)
    cols = len(A[0])
    results = []
    for icols in range(cols):
        total = 0
        for irows in range(rows):
            total += A[irows][icols]
        results.append(total)

    return results