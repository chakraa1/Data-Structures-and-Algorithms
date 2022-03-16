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
A=13
print(NumberOfOneBits(A))