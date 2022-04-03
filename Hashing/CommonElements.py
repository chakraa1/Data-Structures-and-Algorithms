from collections import defaultdict
def solve(A, B):
    ans = []
    freq_map_a = defaultdict(int)
    for a in A:
        freq_map_a[a] += 1
    for b in B:
        if b in freq_map_a and freq_map_a[b] > 0:
            ans.append(b)
            freq_map_a[b] -= 1

    return ans
A = [1, 2, 2, 1]
B = [2, 3, 1, 2]
#A = [2, 1, 4, 10]
#B = [3, 6, 2, 10, 10]
print(solve(A,B))
