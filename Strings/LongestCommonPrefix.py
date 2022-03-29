def LongestCommonPrefix(A):
    n = len(A)
    if n == 0:
        return ""

    if n == 1:
        return A[0]

    min_common_len = float('inf')
    for s in A:
        min_common_len = min(len(s), min_common_len)

    B = sorted(A)

    i = 0
    while i < min_common_len and B[0][i] == B[n - 1][i]:
        i += 1

    return A[0][0:i]

A = ["abcdefgh", "aefghijk", "abcefgh"]
#A = ["abab", "ab", "abcd"]
print(LongestCommonPrefix(A))