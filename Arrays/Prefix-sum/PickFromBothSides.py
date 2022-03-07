def PickFromBothSidesArray(A,B):
    ans=0
    n=len(A)
    print("array length ",n,B)
    if n < B:
        for elem in range(n):
            ans +=elem
        return ans
    p=[A[0]]
    for item in A[1:]:
        p.append(item+p[-1])

    s = [0 for _ in range(n)]
    s[n - 1] = A[n - 1]
    for i in range(n-2,-1,-1):
        s[i] = s[i + 1] + A[i]
    print(A,p,s)
    for j in range(B+1):
        if j==0:
            new_sum=s[-B]
        elif j==B:
            new_sum=p[B-1]
        else:
            new_sum = p[j-1]+s[-(B-j)]
        if new_sum > ans:
            ans=new_sum
    return ans
#A = [5, -2, 3 , 1, 2,4]
#B = 3
A=[ -969, -948, 350, 150, -59, 724, 966, 430, 107, -809, -993, 337, 457, -713, 753, -617, -55, -91, -791, 758, -779, -412, -578, -54, 506, 30, -587, 168, -100, -409, -238, 655, 410, -641, 624, -463, 548, -517, 595, -959, 602, -650, -709, -164, 374, 20, -404, -979, 348, 199, 668, -516, -719, -266, -947, 999, -582, 938, -100, 788, -873, -533, 728, -107, -352, -517, 807, -579, -690, -383, -187, 514, -691, 616, -65, 451, -400, 249, -481, 556, -202, -697, -776, 8, 844, -391, -11, -298, 195, -515, 93, -657, -477, 587 ]
B=81
# NOTE: Suppose B = 4 and array A contains 10 elements then
#
# You can pick first four elements or can pick last four elements or can pick 1 from front and 3 from back etc .
# you need to return the maximum possible sum of elements you can pick.

# Pick element 5 from front and element (1, 2)
# from back so we get 5 + 1 + 2 = 8
print("ans is -->",PickFromBothSidesArray(A,B))
