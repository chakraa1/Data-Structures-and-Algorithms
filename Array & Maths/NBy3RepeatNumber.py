"""
===================
Problem Description
===================
You're given a read-only array of N integers. Find out if any integer occurs more than N/3 times in the array in linear time and constant additional space.
If so, return the integer. If not, return -1.
If there are multiple solutions, return any one.

===================
Problem Constraints
===================
1 <= N <= 7*105
1 <= A[i] <= 109

===================
Input Format
===================
The only argument is an integer array A.

===================
Output Format
===================
Return an integer.

===================
Example Input
===================
[1 2 3 1 1]

Example Output 1
===================
Example Explanation
===================
1 occurs 3 times which is more than 5/3 times.

"""
def NBy3RepeatNumber(A):
    me1, me2 = A[0], 0
    f1, f2 = 1, 0
    n = len(A)
    for i in range(1,n):
        if A[i] == me1:
            f1 += 1
        elif A[i] == me2:
            f2 += 1
        elif A[i] != me1 and f2 == 0:
            me2 = A[i]
            f2 = 1
        elif A[i] != me2 and f1 == 0:
            me1 = A[i]
            f1 = 1
        elif A[i] != me1 and A[i] != me2:
            if f1 > 0:
                f1 -= 1
            if f2 > 0:
                f2 -= 1

    me1_cnt = 0
    me2_cnt = 0

    for x in A:
        if me1 == x:
            me1_cnt += 1
        if me2 == x:
            me2_cnt += 1

    if me1_cnt > n/3:
        return me1
    elif me2_cnt > n/3:
        return me2

    return -1
A= [1,2,3,1,1]
print(NBy3RepeatNumber(A))