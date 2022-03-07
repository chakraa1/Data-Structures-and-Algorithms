def rangeSum(A,B):
    result=[]
    p=[A[0]]
    for x in A[1:]:
        p.append(p[-1]+x)
    for i in range(len(B)):
        start,end=B[i][0],B[i][1]
        print(start,end,end=" ")
        cal_sum=0
        if start==1:
            cal_sum=p[end-1]
        else:
            cal_sum=p[end-1]-p[start-2]
        result.append(cal_sum)
    return result
#A = [1, 2, 3, 4, 5]
#B = [[1, 4], [2, 3]]

#A = [2, 2, 2]
#B = [[1, 1], [2, 3]]
A=[ 8, 1, 2, 9, 4, 9, 1, 4, 4 ]
B=[[2,8]]
print(rangeSum(A,B))