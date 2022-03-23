"""
++++++++++++++++++++
Moore's  Algorithm
++++++++++++++++++++

===================
Problem Description
===================
Given an array of size N, find the majority element. The majority element is the element that appears more than floor(n/2) times.
You may assume that the array is non-empty and the majority element always exists in the array.

===================
Problem Constraints
===================
1 <= N <= 5*105
1 <= num[i] <= 109

===================
Input Format
===================
Only argument is an integer array.

===================
Output Format
===================
Return an integer.

===================
Example Input
===================
[2, 1, 2]

===================
Example Output
===================
2

===================
Example Explanation
===================
2 occurs 2 times which is greater than 3/2.

"""
def MajorityElement(A):
    me = A[0]
    freq = 1
    n = len(A)
    for i in range(1,n):
        x = A[i]
        if x == me:
            freq += 1
        elif freq == 0:
            me = x
            freq = 1
        elif x != me:
            if freq > 0:
                freq -= 1
            else:
                me = x
                freq = 1

    me_count = 0
    for x in A:
        if x == me:
            me_count += 1

    if me_count > n/2:
        return me
    else:
        return "No Majority"

A = [2, 3,4,3, 2,3,3,1,3,3,5,3,2,3]
print(MajorityElement(A))