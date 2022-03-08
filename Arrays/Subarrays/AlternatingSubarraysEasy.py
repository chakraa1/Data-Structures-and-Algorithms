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
    alternating_subarray_indices = []
    subrray_length = 2 * B + 1
    n = len(A)

    if subrray_length == 1:
        for i in range(n):
            alternating_subarray_indices.append(i)
        return alternating_subarray_indices

    for start in range(n - subrray_length + 1):
        end = subrray_length + start - 1
        subarray = A[start:end + 1]
        isAlt = True
        previous_element = subarray[0]
        for i in range(1, len(subarray)):
            if previous_element == subarray[i]:
                isAlt = False
            previous_element = subarray[i]
        if isAlt:
            alternating_subarray_indices.append((start + end) // 2)

    return alternating_subarray_indices
def AlternatingSubarraysOrderN(A,B):
    alternating_subarray_indices = []
    subrray_length = 2 * B + 1
    n = len(A)

    if subrray_length == 1:
        for i in range(n):
            alternating_subarray_indices.append(i)
        return alternating_subarray_indices


    return alternating_subarray_indices
A = [1, 0, 1, 0, 1]
B = 1
# Output - [1, 2, 3]
print(AlternatingSubarraysEasyBruteForce(A,B))

#A = [0, 0, 0, 1, 1, 0, 1]
#B = 0
# Output - [0, 1, 2, 3, 4, 5, 6]
#print(AlternatingSubarraysEasyBruteForce(A,B))
print(AlternatingSubarraysEasyOptimised(A,B))