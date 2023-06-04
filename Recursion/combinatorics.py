def ncr(n,r):
    if r == 0 or n == r:
        return 1
    return ncr(n-1,r-1) + ncr(n-1,r)
n = 3
r = 2
print(ncr(n,r))
