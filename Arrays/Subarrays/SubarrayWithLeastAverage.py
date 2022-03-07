def SubArrayWithLeastAverageBruteForce(A, B):
    n=len(A)
    avg = sum(A)//n
    ans=-1
    for s in range(n-B+1):
        e=B+s-1
        total=0
        for i in range(s,e+1):
          total +=A[i]
        avg_b_size=total//B
        if avg_b_size < avg:
            ans=s
    return ans
def SubArrayWithLeastAveragePrefixSum(A,B):
    n = len(A)
    avg = sum(A) // n
    ans = -1
    p = [A[0]]
    for x in A[1:]:
        p.append(p[-1] + x)
    for s in range(n - B + 1):
        e = B + s - 1
        total=0
        if s==0:
            total=p[e]
        else:
            total = p[e]-p[s-1]
        avg_b_size = total // B
        if avg_b_size < avg:
            ans = s
    return ans

def SubArrayWithLeastAverageOptimize(A, B):
    n = len(A)
    ans = 0
    total = 0
    for x in range(B):
        total += A[x]
    avg = total / B
    ans = 0
    for s in range(1, n - B + 1):
        e = B + s - 1
        total = (total + A[e] - A[s - 1])
        avg_b_size = total / B
        if avg_b_size < avg:
            ans = s
            avg = avg_b_size
    return ans
A=[3, 7, 90, 20, 10, 50, 40]
B=3
A=[3, 7, 5, 20, -10, 0, 12]
B=2
A=[ 18, 11, 16, 19, 11, 9, 8, 15, 3, 10, 9, 20, 1, 19 ]
B=1
A =[ 20, 3, 13, 5, 10, 14, 8, 5, 11, 9, 1, 11 ]
B = 9

print(SubArrayWithLeastAverageBruteForce(A,B))
print(SubArrayWithLeastAveragePrefixSum(A,B))
print(SubArrayWithLeastAverageOptimize(A,B))