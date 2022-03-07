def SumAllSubarrays(A):
    ans = 0
    n = len(A)
    p=[A[0]]
    for x in A[1:]:
        p.append(x+p[-1])
    for s in range(n):
        for e in range(s,n):
            if s==0:
                ans+=p[e]
            else:
                ans +=p[e]-p[s-1]
    return ans
def SumAllSubarraysOptimal(A):
    ans = 0
    n = len(A)
    for i in range(n):
        ans +=A[i]*(i+1)*(n-i)
    return ans
# A=[2,1,0,-6,8,3,2,4]
A = [1, 2, 3]
#A = [2, 1, 3]
#A=[ 2, 9, 5 ]
print(SumAllSubarrays(A))
print(SumAllSubarraysOptimal(A))