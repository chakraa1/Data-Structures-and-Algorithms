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
    """
    ============
    Approach
    ============
    Check IF most significant bit(left most) is 1 in at least 4 of them. If yes then select
    those numbers (having MSB = 1) and remove rest of them and also remove left most bit.
    ELSE there are less than 4 numbers having most significant bit 1 then keep all of them
    and remove most significant bit from all of them. And repeat until there are 0 bits left.

    This way you’ll get solution in N*log(K) where K is the MAX value of input number.

    """
    maxSatisfaction = 0

    for i in reversed(range(31)): # why range 31 - because we're ignoring signed bit of 32 bit integer
        bestcaseMSB = maxSatisfaction | (1 << i)
        countBestCaseMSB = 0

        for k in range(len(A)):
            if A[k] & bestcaseMSB == bestcaseMSB:
                countBestCaseMSB += 1

            if countBestCaseMSB >= 4:
                maxSatisfaction = bestcaseMSB

    return maxSatisfaction
A = [10, 20, 15, 4, 14]
A = [2, 2, 7, 15]
print(MaximumSatisfaction(A))
