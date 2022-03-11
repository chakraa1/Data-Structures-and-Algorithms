def PrintSpiralMatrix(N,M):
    MAT=[[0]*M for _ in range(N)]
    element=0

    for c in range(M):
        for r in range(N):
            MAT[r][c] = element
            element +=1

    # Current position
    r, c = 0, 0
    direction = 'right'
    while(N*M):
        print(MAT[r][c])
        if direction == 'right': # Moving right
            # Change direction if boundary is being hit
            if c == M-1:
                direction = 'down'
                r += 1
            else:
                c += 1
        elif direction == 'left': # Moving left
            if c == 0:
                direction = 'up'
                r -= 1
            else:
                c -= 1
        elif direction == 'down': # Moving down
            if r == N-1:
                direction = 'left'
                c -= 1
            else:
                r += 1
        elif direction == 'up':  # Moving up
            if r == 1:
                # break
                direction = 'right'
                c += 1
            else:
                r -= 1
    return MAT
N=5
M=10
print(PrintSpiralMatrix(N,M))
