"""
Determine if a Sudoku is valid, according to: http://sudoku.com.au/TheRules.aspx
The Sudoku board could be partially filled, where empty cells are filled with the character '.'.
The input corresponding to the above configuration :

["53..7....", "6..195...", ".98....6.", "8...6...3", "4..8.3..1", "7...2...6", ".6....28.", "...419..5", "....8..79"]
A partially filled sudoku which is valid.

========
Note:
========
A valid Sudoku board (partially filled) is not necessarily solvable. Only the filled cells need to be validated.
Return 0 / 1 ( 0 for false, 1 for true ) for this problem

"""
def isValidSudoku(A):
    sudoku_set = set()

    for i in range(0, 9):
        for j in range(0, 9):
            curr_val = A[i][j]
            if curr_val != '.':
                if (curr_val + " R " + str(i)) in sudoku_set or (curr_val + " C " + str(j)) in sudoku_set or (
                        curr_val + " B " + str(i // 3) + "-" + str(j // 3)) in sudoku_set:
                    return 0
                sudoku_set.add(curr_val + " R " + str(i))
                sudoku_set.add(curr_val + " C " + str(j))
                sudoku_set.add(curr_val + " B " + str(i // 3) + "-" + str(j // 3))

    return 1