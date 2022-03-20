"""
====================
Problem Description
====================
Given an array of integers A, a subarray of an array is said to be good if it fulfills any one of the criteria:
1. Length of the subarray is be even, and the sum of all the elements of the subarray must be less than B.
2. Length of the subarray is be odd, and the sum of all the elements of the subarray must be greater than B.
Your task is to find the count of good subarrays in A.

====================
Problem Constraints
====================
1 <= len(A) <= 103
1 <= A[i] <= 103
1 <= B <= 107

====================
Input Format
====================
The first argument given is the integer array A.
The second argument given is an integer B.

====================
Output Format
====================
Return the count of good subarrays in A.

====================
Example Input
====================
Input 1: A = [1, 2, 3, 4, 5] , B = 4
Input 2: A = [13, 16, 16, 15, 9, 16, 2, 7, 6, 17, 3, 9] , B = 65

====================
Example Output
====================
Output 1: 6
Output 2: 36

====================
Example Explanation
====================
Explanation 1: Even length good subarrays = {1, 2}
Odd length good subarrays = {1, 2, 3}, {1, 2, 3, 4, 5}, {2, 3, 4}, {3, 4, 5}, {5}

"""
def CountingGoodSubarrays(A,B):
    print(A)
    count=0
    p=[A[0]]
    for x in A[1:]:
        p.append(x+p[-1])
    n=len(A)
    print(p)
    for s in range(len(A)):
        total=0
        subrray_length=0
        for e in range(s,n):
            subrray_length=e-s+1
            if s==0:
                total=p[e]
            else:
                total=p[e]-p[s-1]
            if ((subrray_length%2==0 and total <B) or (subrray_length %2 !=0 and total >B)):
                print("subarray", A[s:e + 1], "sum", total, "subrray_length", subrray_length, "B", B)
                count += 1

    return count
A = [1, 2, 3, 4, 5]
B = 4
print(CountingGoodSubarrays(A,B))
A = [13, 16, 16, 15, 9, 16, 2, 7, 6, 17, 3, 9]
B = 65
print(CountingGoodSubarrays(A,B))