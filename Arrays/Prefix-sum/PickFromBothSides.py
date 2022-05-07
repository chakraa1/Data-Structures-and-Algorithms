def PickFromBothSidesArray(A,B):
    maxSum = 0
    n = len(A)
    if n < B:
        for x in A:
            maxSum += x
        return maxSum
    """
    Creating prefix sum array 
    """
    p = [A[0]]
    for item in A[1:]:
        p.append(item+p[-1])

    """
    Creating suffix sum array 
    """
    s = [0] * n
    s[n - 1] = A[n - 1]
    for i in reversed(range(n - 1)):
        s[i] = s[i + 1] + A[i]

    """
    Case # 1  - Take all B elements from First
    Case # 2  - Take all B elements from Last
    Case # 3  - Take i from first and  B -i elements from Last
    """

    for i in range(B):
        Sum = 0
        if i == B:              # Case 1
            Sum = p[i-1]
        elif i == 0:            # Case 2
            Sum = s[-B]
        else:                   # Case 3
            Sum = p[i-1] + s[-(B-i)]

        maxSum = max(Sum,maxSum)

    return maxSum
A = [5, -2, 3 , 1, 2]
B = 3
#A=[ -969, -948, 350, 150, -59, 724, 966, 430, 107, -809, -993, 337, 457, -713, 753, -617, -55, -91, -791, 758, -779, -412, -578, -54, 506, 30, -587, 168, -100, -409, -238, 655, 410, -641, 624, -463, 548, -517, 595, -959, 602, -650, -709, -164, 374, 20, -404, -979, 348, 199, 668, -516, -719, -266, -947, 999, -582, 938, -100, 788, -873, -533, 728, -107, -352, -517, 807, -579, -690, -383, -187, 514, -691, 616, -65, 451, -400, 249, -481, 556, -202, -697, -776, 8, 844, -391, -11, -298, 195, -515, 93, -657, -477, 587 ]
#B=81

A = [1, 2]
B = 4
# NOTE: Suppose B = 4 and array A contains 10 elements then
#
# You can pick first four elements or can pick last four elements or can pick 1 from front and 3 from back etc .
# you need to return the maximum possible sum of elements you can pick.

# Pick element 5 from front and element (1, 2)
# from back so we get 5 + 1 + 2 = 8
print("ans is -->",PickFromBothSidesArray(A,B))
