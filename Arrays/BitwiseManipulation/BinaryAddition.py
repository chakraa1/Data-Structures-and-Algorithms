def binary_addition(A,B):
    ans = ''
    max_digit_length = max(len(A),len(B))
    A = A.zfill(max_digit_length)
    B = B.zfill(max_digit_length)

    carry_fwd = 0
    for digit_index in reversed(range(max_digit_length)):
        resulted_digit = carry_fwd

        resulted_digit += 1 if A[digit_index] == '1' else 0
        resulted_digit += 1 if B[digit_index] == '1' else 0

        if resulted_digit % 2 == 1:  # for 1 and 3 (including carry forward)
            ans = '1' + str(ans)
        else:
            ans = '0' + str(ans)

        carry_fwd = 1 if resulted_digit > 1 else 0

    if carry_fwd != 0:
        ans = '1' + str(ans)

    return ans
A = "0100"
B = "10"
A = "1010110111001101101000"
B = "1000011011000000111100110"
print(binary_addition(A,B))