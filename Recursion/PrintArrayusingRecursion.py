def printArrayRecursion(A,n):
    helper(A,0,n)

def helper(A,start,end):
    if start == end:
        return
    print(A[start])
    helper(A,start+1,end)

A1 = [1,6,9,5]
n = len(A1)
print(printArrayRecursion(A1),n)