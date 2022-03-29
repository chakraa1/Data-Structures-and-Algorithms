def solve(A):
    cnt = 0
    prev_1 = None
    prev_2 = None
    for char in A:
        if char == 'b' and prev_1 == 'o' and prev_2 == 'b':
            cnt += 1

        prev_2 = prev_1
        prev_1 = char

    return cnt
A ="bobabtbobl"
print(solve(A))