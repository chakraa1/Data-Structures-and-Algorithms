def generateMatrix(A):
    matrix_S = [[0] * A for _ in range(A)]
    r, c = 0, 0
    direction = 'right'
    counter=1
    for _ in range(A ** 2):
        matrix_S[r][c] = counter
        counter += 1
        if direction == 'right':
            if c == A-1:
                r += 1
                direction = 'left'
            else:
                c += 1
        elif direction == 'left':
            if c == 0:
                direction = 'right'
                r += 1
            else:
                c -= 1

    for row in range(A):
        for col in range(A):
            print(matrix_S[row][col],end=" ")
        print()

    return 0
A=3
print(generateMatrix(A))
