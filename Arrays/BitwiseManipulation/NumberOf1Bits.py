"""
====================
Problem Description
====================
Write a function that takes an integer and returns the number of 1 bits it has.

====================
Problem Constraints
====================
1 <= A <= 109

====================
Input Format
====================
First and only argument contains integer A

Input1: 11

====================
Example Output
====================
Output1: 3

Example Explanation

Explaination1:
11 is represented as 1011 in binary.

"""
def NumberOfOneBits(A):
    count = 0
    while A :
        count += A & 1
        A >>= 1
    return count


def countSetBitsLeftShift(x):
    cnt = 0
    k = 0
    while True:
        if x & (1 << k) != 0:
            cnt += 1
        k += 1

        if x < (1 << k):
            break
    return cnt

# count of bits = log2(x) + 1

# 01001010100101
# 10000000000000

# x & (1 << 0)
# x & (1 << 1)
# ...
# x & (1 << k)
def countSetBitsRightShift(x):
  cnt = 0
  while x > 0:
    cnt += x&1
    x = x>>1
  return cnt

# 100001010100101
# 000000000000001

# 100001010100101 >> 1
# 10000101010010
# 00000000000001

A=13
print(NumberOfOneBits(A))
countSetBitsLeftShift(16)
countSetBitsRightShift(1023)