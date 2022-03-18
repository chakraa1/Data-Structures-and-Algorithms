"""
=====================
Problem Description
=====================
Given an array of integers A of size N denoting the quality of the fruits. A[i] represents the fruit quality of
the ith fruit.
Shaun needs to pick four fruits, but he needs to pick them so that his satisfaction value will be maximum.
If a, b, c, and d are fruit quality of the four fruits picked,
then the satisfaction value(a, b, c, d) = (a & b & c & d) where & is bitwise AND operator.

Find the maximum satisfaction value Shaun can obtain.

=====================
Problem Constraints
=====================
4 <= N <= 105
1 <= A[i] <= 2 * 109

=====================
Input Format
=====================
The only argument given is the integer array A.

=====================
Output Format
=====================
Return the maximum satisfaction value Shaun can obtain.

=====================
Example Input
=====================
Input 1: A = [10, 20, 15, 4, 14]
Input 2: A = [2, 2, 7, 15]

=====================
Example Output
=====================
Output 1: 4
Output 2: 2

=====================
Example Explanation
=====================
Explanation 1: Shaun can pick fruits with fruits quality 20, 15, 4, 14 and satisfaction value is (20 & 15 & 4 & 15) = 4
Explanation 2: Shaun will pick fruits with fruits quality 2, 2, 7, 15 and satisfaction value is(2 & 2 & 7 & 15) = 2
"""

def MaximumSatisfaction(A):
    maxSatisfactionvalue=0

    """
    Goal is to SET most significant bit(i.e. MSB) (for maximizing satisfaction) for at least 4 quantities 
    simultaneously as "a & b & c & d" operation to be performed .
    If there are k numbers whose MSB is active and remaining n-k numbers in which the bit is zero
    we can ignore n-k numbers as those are anyway not going to contribute for max statisfaction
    """
    commonSetBitIndex=-1

    for i in reversed(range(31)): # why range 31 - because we're ignoring signed bit of 32 bit integer
        countActiveMSB=0
        for k in range(len(A)):
            if A[k] & (1 << i) > 0:
                countActiveMSB += 1

            if countActiveMSB >= 4:
                commonSetBitIndex = i
                break
    # Now check if common set bit is on for which quantities i.e. input numbers in the array
    for element in A:
        if element & (1 << commonSetBitIndex):
            maxSatisfactionvalue += 1

    return maxSatisfactionvalue

A = [10, 20, 15, 4, 14]
A = [2, 2, 7, 15]
print(MaximumSatisfaction(A))