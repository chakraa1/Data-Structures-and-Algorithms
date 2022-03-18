"""
=====================
Problem Description
=====================
Given an array of positive integers A, two integers appear only once, and all the other integers appear twice.
Find the two integers that appear only once.

=====================
Problem Constraints
=====================
2 <= |A| <= 100000
1 <= A[i] <= 109

=====================
Input Format
=====================
The first argument is an array of integers of size N.

=====================
Output Format
=====================
Return an array of two integers that appear only once.

=====================
Example Input
=====================
Input 1: A = [1, 2, 3, 1, 2, 4]
Input 2: A = [1, 2]

=====================
Example Output
=====================
Output 1: [3, 4]
Output 2: [1, 2]

=====================
Example Explanation
=====================
Explanation 1: 3 and 4 appear only once.
Explanation 2: 1 and 2 appear only once.

"""
def SingleNumberIII(A):
    num1,num2 = 0,0

    # As there are two not unique element then xor of all product will xor of A,B
    # where A, B are two single elements
    xor_A_B = A[0]
    for i in range(1,len(A)):
        xor_A_B ^= A[i]

    # Need to find any set bit just to differentiate between A & B
    # So let's find first set bit
    set_bit=0
    for j in range(xor_A_B):
        if xor_A_B & (1 << j) > 0:
            set_bit = j
            break

    # Differentiating the numbers
    for element in A:
        if element & (1 << set_bit):
            num1 ^= element
        else:
            num2 ^= element

    return [min(num1,num2),max(num1,num2)]

A = [1, 2, 3, 1, 2, 4]
#A = [1, 2]
print(SingleNumberIII(A))