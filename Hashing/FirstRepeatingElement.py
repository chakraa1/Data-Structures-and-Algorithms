def FirstRepeatingElement(A):
    ans = -1
    freq = dict()

    for i in range(len(A)):
        if A[i] in freq:
            freq[A[i]] += 1
        else:
            freq[A[i]] = 1
    for x in A:
        if freq[x] > 1:
            ans = x
            break

    return ans

A = [10, 5, 3, 4, 3, 5, 6]
#A = [6, 10, 5, 4, 9, 120]
print(FirstRepeatingElement(A))