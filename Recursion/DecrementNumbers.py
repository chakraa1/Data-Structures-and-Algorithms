def dec(N):
    if N == 1:
        print(1)
    print(N)
    dec(N-1)

N=5
print(dec(N))