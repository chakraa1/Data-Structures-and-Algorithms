def printInc(N):
    if N == 1:
        print(1)
        return

    printInc(N-1)
    print(N)

N = 6
print(printInc(N))