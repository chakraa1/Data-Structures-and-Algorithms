def anti_diagonal(A):
    rows=len(A)
    cols=len(A[0])
    anti_diagonal=[[0]*rows for _ in range(2 * rows - 1)]
    antiDiagRowIndex = 0
    for icol in range(cols):
        r = 0
        c = icol
        antiDiagColIndex = 0
        while(r < rows and c > 0):
           anti_diagonal[antiDiagRowIndex][antiDiagColIndex] = A[r][c]
           r += 1
           c -= 1
           antiDiagColIndex += 1
        anti_diagonal[antiDiagRowIndex][antiDiagColIndex] = A[r][c]
        antiDiagColIndex += 1
        antiDiagRowIndex += 1

    for iRow in range(1,cols):
        r = iRow
        c = cols-1
        antiDiagColIndex = 0
        while(r < rows and c > 0):
           anti_diagonal[antiDiagRowIndex][antiDiagColIndex] = A[r][c]
           r += 1
           c -= 1
           antiDiagColIndex += 1
        antiDiagRowIndex += 1
        antiDiagColIndex += 1

    return anti_diagonal
A=[[1,2,3],[4,5,6],[7,8,9]]
A=[[1,2],[3,4]]
print(anti_diagonal(A))
