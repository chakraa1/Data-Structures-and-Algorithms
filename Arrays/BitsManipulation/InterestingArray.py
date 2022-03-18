"""
====================
Problem Description
====================
You have an array A with N elements. We have two types of operation available on this array :
We can split an element B into two elements, C and D, such that B = C + D.
We can merge two elements, P and Q, to one element, R, such that R = P ^ Q i.e., XOR of P and Q.
You have to determine whether it is possible to convert array A to size 1, containing a single element equal to 0
after several splits and/or merge?

====================
Problem Constraints
====================
1 <= N <= 100000
1 <= A[i] <= 106

====================
Input Format
====================
The first argument is an integer array A of size N.

====================
Output Format
====================
Return "Yes" if it is possible otherwise return "No".

Example Input
Input 1: A = [9, 17]
Input 2: A = [1]

Example Output
Output 1:Yes
Output 2:No
====================
Example Explanation
====================
Explanation 1:

 Following is one possible sequence of operations -
 1) Merge i.e 9 XOR 17 = 24
 2) Split 24 into two parts each of size 12
 3) Merge i.e 12 XOR 12 = 0
 As there is only 1 element i.e 0. So it is possible.

Explanation 2:

 There is no possible way to make it 0.
"""
def InterestingArray(A):
    isInterestingArray = "No"

    """
    =================
    Example : [4, 3]
    =================
    Split 4 into 1+1+1+1
    Then merge (1^1^1^1) --> 0
    Again if we merge 0 ^ 3 --> 3 so the even number vanishes 

    Hence, differentiator is odd number , and we've to find if odd number is present or not 
    if odd element present then Yes , otherwise No 
    
    """
    countOdds = 0
    for x in A:
        # checking array elements is odd
        if x & 1 == 1:
            countOdds += 1

    # Checking total number of odd elements is odd
    if countOdds & 1 != 1:
        isInterestingArray = "Yes"

    return isInterestingArray
A = [9, 17]
A = [1]
print(InterestingArray(A))