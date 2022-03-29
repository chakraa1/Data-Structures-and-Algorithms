def solve(A, B):
    freq =[0]*26
    for char in A:
        code = ord(char) - ord('a')
        freq[code] += 1
    freq_sorted = sorted(freq)

    for i in range(26):
        if freq_sorted[i] != 0:
            if B > 0 and B >= freq_sorted[i]:
                B -= freq_sorted[i]
            else:
                return 26-i

    return 0
A = "abcabbccd"
B = 3
print(solve(A,B))