def CountingGoodSubarrays(A,B):
    print(A)
    count=0
    p=[A[0]]
    for x in A[1:]:
        p.append(x+p[-1])
    n=len(A)
    print(p)
    for s in range(len(A)):
        total=0
        subrray_length=0
        for e in range(s,n):
            subrray_length=e-s+1
            if s==0:
                total=p[e]
            else:
                total=p[e]-p[s-1]
            if ((subrray_length%2==0 and total <B) or (subrray_length %2 !=0 and total >B)):
                print("subarray", A[s:e + 1], "sum", total, "subrray_length", subrray_length, "B", B)
                count += 1

    return count
A = [1, 2, 3, 4, 5]
B = 4
print(CountingGoodSubarrays(A,B))
A = [13, 16, 16, 15, 9, 16, 2, 7, 6, 17, 3, 9]
B = 65
print(CountingGoodSubarrays(A,B))