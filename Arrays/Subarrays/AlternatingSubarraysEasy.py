"""
Q3. Alternating Subarrays Easy

===================
Problem Description
===================
You are given an integer array A of length N comprising of 0's & 1's, and an integer B.
You have to tell all the indices of array A that can act as a center of 2 * B + 1 length 0-1 alternating subarray.
A 0-1 alternating array is an array containing only 0's & 1's, and having no adjacent 0's or 1's.
For e.g. arrays [0, 1, 0, 1], [1, 0] and [1] are 0-1 alternating, while [1, 1] and [0, 1, 0, 0, 1] are not.

===================
Problem Constraints
===================
1 <= N <= 105
A[i] equals to 0 or 1.
0 <= B <= (N - 1) / 2

===================
Input Format
===================
First argument is an integer array A.
Second argument is an integer B.
===================
Output Format
===================
Return an integer array containing indices(0-based) in sorted order.
If no such index exists, return an empty integer array.

===================
Example Input
===================
Input 1:

 A = [1, 0, 1, 0, 1]
 B = 1

Input 2:

 A = [0, 0, 0, 1, 1, 0, 1]
 B = 0

===================
Example Output
===================
Output 1:

 [1, 2, 3]
Output 2:

 [0, 1, 2, 3, 4, 5, 6]

===================
Example Explanation
===================
Explanation 1:

 Index 1 acts as a centre of alternating sequence: [A0, A1, A2]
 Index 2 acts as a centre of alternating sequence: [A1, A2, A3]
 Index 3 acts as a centre of alternating sequence: [A2, A3, A4]

Explanation 2: Each index in the array acts as the center of alternating sequences of lengths 1.

"""
def AlternatingSubarraysEasyBruteForce(A,B):
    result=[]
    k=2*B+1
    n=len(A)
    if k==1:
        for i in range(n):
            result.append(i)
        return result
    for s in range(n-k+1):
        e=k+s-1
        subarray=A[s:e+1]
        isAlternativeArray=True
        previous_element=subarray[0]
        for i in range(1,len(subarray)):
            if previous_element==subarray[i]:
                isAlternativeArray = False
            previous_element=subarray[i]
        if isAlternativeArray:
            result.append((s+e)//2)
        print(subarray)
    return result

def AlternatingSubarraysEasyOptimised(A,B):
    alternating_subarray_indices = []
    subrray_length = 2 * B + 1
    n = len(A)

    if subrray_length == 1:
        for i in range(n):
            alternating_subarray_indices.append(i)
        return alternating_subarray_indices

    for start in range(n - subrray_length + 1):
        end = subrray_length + start - 1
        subarray = A[start:end + 1]
        isAlt = True
        previous_element = subarray[0]
        for i in range(1, len(subarray)):
            if previous_element == subarray[i]:
                isAlt = False
            previous_element = subarray[i]
        if isAlt:
            alternating_subarray_indices.append((start + end) // 2)

    return alternating_subarray_indices
def AlternatingSubarraysOrderN(A,B):
    ans = []

    n = len(A)
    k = 2 * B + 1
    l,r = 0,0

    while r < n:
        if r == 0 or A[r] != A[r-1]: # Comparing with previous element but not with next element
            r += 1
        else:
            l = r # When no alternating sub array sequence, then next sequence should start from current index
            r += 1

        subarray_length = r - l  # Because l,r are not both inclusive
        if subarray_length == k:
            ans.append(l+B) # as k is 2B +1 , middle element would be i+B the element
            l += 1 # Update left pointer to start next sequence

    return ans
A = [1, 0, 1, 0, 1]
B = 1
# Output - [1, 2, 3]
#print(AlternatingSubarraysEasyBruteForce(A,B))

A = [0, 0, 0, 1, 1, 0, 1]
B = 0
print(AlternatingSubarraysOrderN(A,B))