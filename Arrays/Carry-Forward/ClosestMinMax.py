import math
def ClosestMinMaxBruteForce(A):
    inf=math.inf
    max=-inf
    min=inf
    for elem in A:
        if elem > max:
            max=elem
        elif elem < min:
            min=elem
    n=len(A)
    min_lenth=inf
    for start in range(n):
            for end in range(start,n):
                has_max=False
                has_min=False
                subarray_length=0
                for i in range(start,end+1):
                    if A[i] == max:
                        has_max=True
                    if A[i] == min:
                        has_min=True

                if has_max and has_min:
                    subarray_length=end-start+1
                    if subarray_length < min_lenth:
                        min_lenth=subarray_length
    return min_lenth
def ClosestMinMaxOptimize(A):
    max=0
    min=2001

    for i in range(len(A)):
        if A[i] > max:
            max=A[i]
        elif A[i] < min:
            min=A[i]

    min_subarray_length=len(A)
    has_max=False
    has_min=False
    max_index=0
    min_index=0
    for i in reversed(range(len(A))):
        subarray_length=0
        if A[i] == max:
            has_max=True
            max_index=i
        if A[i] == min:
            has_min=True
            min_index=i
        if has_max and has_min:
            subarray_length=max_index-min_index
            if subarray_length <0:
                subarray_length *= -1
            subarray_length += 1
            if subarray_length < min_subarray_length:
                min_subarray_length=subarray_length
    return min_subarray_length

    return min_lenth
def ClosestMinMaxOptimizeEffecient(A):
    min_length=float('inf')

    max_val = max(A)
    min_val = min(A)

    min_index=-1
    max_index=-1

    for i in range(len(A)):
        if A[i]==min_val:
            min_index=i
            if max_index !=-1:
                l=min_index-max_index+1
                min_length=min(l,min_length)

        if A[i]==max_val:
            max_index=i
            if max_index !=1:
                l=max_index-min_index+1
                min_length=min(l,min_length)

    return min_length

A = [1, 3,2,5,8,1,4,8]
A2=[ 814, 761, 697, 483, 981 ]
A3=[ 343, 291, 963, 165, 152 ]
print(ClosestMinMaxBruteForce(A))
print(ClosestMinMaxOptimize(A))
print(ClosestMinMaxOptimizeClassDiscussion(A))
print(ClosestMinMaxBruteForce(A2))
print(ClosestMinMaxOptimize(A2))
print(ClosestMinMaxOptimizeClassDiscussion(A2))
print(ClosestMinMaxBruteForce(A3))
print(ClosestMinMaxOptimize(A3))
print(ClosestMinMaxOptimizeClassDiscussion(A3))
