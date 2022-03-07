def AlternatingSubarraysEasyBruteForce(A,B):
    result=[]
    k=2*B+1
    n=len(A)
    if k==1:
        for i in range(n):
            result.append(i)
        return result
    for s in range(n-k+1):
        e=k+s-1
        subarray=A[s:e+1]
        isAlternativeArray=True
        previous_element=subarray[0]
        for i in range(1,len(subarray)):
            if previous_element==subarray[i]:
                isAlternativeArray = False
            previous_element=subarray[i]
        if isAlternativeArray:
            result.append((s+e)//2)
        print(subarray)
    return result

def AlternatingSubarraysEasyOptimised(A,B):
    result=[]
    k=2*B+1
    n=len(A)
    if k==1:
        for i in range(n):
            result.append(i)
        return result
    for s in range(n-k+1):
        e=k+s-1
        subarray=A[s:e+1]
        isAlternativeArray=True
        # Check alternative array optimized
        
        if isAlternativeArray:
            result.append((s+e)//2)
        print(subarray)
    return result
A = [1, 0, 1, 0, 1]
B = 1
# Output - [1, 2, 3]
print(AlternatingSubarraysEasyBruteForce(A,B))

A = [0, 0, 0, 1, 1, 0, 1]
B = 0
# Output - [0, 1, 2, 3, 4, 5, 6]
print(AlternatingSubarraysEasyBruteForce(A,B))