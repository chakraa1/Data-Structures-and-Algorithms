def SubSequencePattern(A,B,C):
    count=0
    gCount=0
    for i in reversed(range(len(A))):
        if A[i] == 'G':
            gCount +=1

        if A[i] == 'A':
            count +=gCount
        print(A[i])
    return count
A = "ABCGAG"
B="A"
C="G"
#A = "GAB"
print(SubSequencePattern(A,B,C))