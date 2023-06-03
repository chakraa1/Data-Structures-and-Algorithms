def countDigits(n):
    count = 0
    if n == 0:
        return 0
    return countDigits(n//10) + 1
n = 99999
n = 53
print(countDigits(n))