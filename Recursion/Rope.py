def rope(n,a,b,c):
    if n == 0:
        return 0
    elif n <= 0:
        return -1
    res = max(rope(n-a,a,b,c),rope(n-b,a,b,c),rope(n-c,a,b,c))

    if res == -1:
        return -1
    return res + 1

n = 5
a= 2
b =5
c = 1
# o/p - 5
n = 5
a= 4
b =2
c = 6
# o/p - -1
n = 23
a= 12
b =9
c = 11
# o/p - 2
print(rope(n, a,b,c))