"""
===================
Problem Description
===================
Given an integer array A, find if an integer p exists in the array such that the number of integers greater than p
in the array equals p.

===================
Problem Constraints
===================
1 <= |A| <= 2*105
1 <= A[i] <= 107

===================
Input Format
===================
First and only argument is an integer array A.

===================
Output Format
===================
Return 1 if any such integer p is present else, return -1.

===================
Example Input
===================
Input 1: A = [3, 2, 1, 3]
Input 2: A = [1, 1, 3, 3]

===================
Example Output
===================
Output 1: 1
Output 2: -1

===================
Example Explanation
===================
Explanation 1: For integer 2, there are 2 greater elements in the array..
Explanation 2: There exist no integer satisfying the required conditions.

"""
def NobleInteger(A):
    ans = -1
    noble = 0

    B = sorted(A,reverse=True)

    greater = 0
    prev_element = 0
    prev_element_i = 0
    for i,x in enumerate(B):
        if x == prev_element: # If duplicate , just refer previous index
            greater = prev_element_i
        else:
            greater = i
            prev_element = x
            prev_element_i = i

        if greater == x:
            noble += 1
    if noble > 0:
        ans = 1
    return ans
A = [3, 2, 1, 3]
A = [1, 1, 3, 3]
print(NobleInteger(A))