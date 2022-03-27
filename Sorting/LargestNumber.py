"""
===================
Problem Description
===================
Given an array A of non-negative integers, arrange them such that they form the largest number.
Note: The result may be very large, so you need to return a string instead of an integer.

===================
Problem Constraints
===================
1 <= len(A) <= 100000
0 <= A[i] <= 2*109

===================
Input Format
===================
The first argument is an array of integers.
===================
Output Format
===================
Return a string representing the largest number.

===================
Example Input
===================
Input 1: A = [3, 30, 34, 5, 9]
Input 2: A = [2, 3, 9, 0]

===================
Example Output
===================
Output 1: "9534330"
Output 2: "9320"

===================
Example Explanation
===================
Explanation 1: Reorder the numbers to [9, 5, 34, 3, 30] to form the largest number.
Explanation 2: Reorder the numbers to [9, 3, 2, 0] to form the largest number 9320.

"""
from functools import cmp_to_key
def customSort(a,b):
    x = int(str(a) + str(b))       # digit a followed by b
    y = int(str(b) + str(a))       # digit b followed by a
    """
    a,b digit arrangements 
    a  <-  b --> return -1 [Case A]
    b  ->  a --> return  1 [Case B]
    a  ==  b --> return  0 [Case C]
    """
    if x < y:        # i.e. CASE B
        return 1     # digit a must be left of b
    elif x > y:      # i.e. Case A
        return -1    # digit a must be right of b
    else:
        return 0

def LargestNumber(A):
    ans = ''

    """
     For edge case check if all elements of the input
     arrays are same and that is zero 
    """
    zeroCnt = 0
    for x in A:
        if x == 0:
            zeroCnt += 1
    if zeroCnt == len(A):
        return '0'
    else:
        """
        custom comparator 
        """
        # B = list(map(str,A))
        B = sorted(A,key=cmp_to_key(customSort))

        for x in B:
            ans += str(x)

    return ans
A = [3, 30, 34, 5, 9]
#A = [0, 0, 0, 0]
#A = [2, 3, 9, 0]

print(LargestNumber(A))