def AmazingSubArray(S):
    count=0
    n=len(S)
    vowels=('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
    for i in range(len(S)):
        if S[i] in vowels:
            count +=n-i
    return count
S="ABEC"
print(AmazingSubArray(S))