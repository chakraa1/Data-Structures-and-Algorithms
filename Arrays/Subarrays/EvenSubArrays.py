def solve(A):
    ans = "NO"
    n = len(A)
    if n % 2 == 0 and A[0] % 2 == 0 and A[n - 1] % 2 == 0:
        ans = "YES"
    return ans
A = [2, 4, 8, 6]
#A = [2, 4, 8, 7, 6]
print(solve(A))