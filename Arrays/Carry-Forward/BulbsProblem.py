def bulbs(A):
    count = 0
    flag = 0
    for i in range(len(A)):
        if flag == 0:
            if A[i] == 0:
                count += 1
                flag = 1
        else:
            if A[i] == 1:
                count += 1
                flag = 0
    return count
A = [0, 1, 0, 1]
A2 = [1, 1, 1, 1]
A3 = [1, 0, 0, 1]
A4 = [1, 0, 1, 0]
A5 = [0, 0, 0, 1]
A6 = [0, 0, 1, 0]
A7 = [0, 1, 0, 0]
A8 = [1, 0, 0, 0]
A9 = [1, 0, 0, 1]

#print(bulbs(A))
print("result",bulbs(A8))