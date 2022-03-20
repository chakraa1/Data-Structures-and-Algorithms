"""
====================
Problem Description
====================
You are given an integer array A of length N.
You have to find the sum of all subarray sums of A.
More formally, a subarray is defined as a contiguous part of an array which we can obtain by deleting zero or more elements from either end of the array.
A subarray sum denotes the sum of all the elements of that subarray.

====================
Problem Constraints
====================
1 <= N <= 105
1 <= Ai <= 10 4

====================
Input Format
====================
The first argument is the integer array A.

====================
Output Format
====================
Return a single integer denoting the sum of all subarray sums of the given array.

====================
Example Input
====================
Input 1: A = [1, 2, 3]
Input 2: A = [2, 1, 3]

====================
Example Output
====================
Output 1: 20
Output 2: 19

"""
def SumAllSubarrays(A):
    ans = 0
    n = len(A)
    p=[A[0]]
    for x in A[1:]:
        p.append(x+p[-1])
    for s in range(n):
        for e in range(s,n):
            if s==0:
                ans+=p[e]
            else:
                ans +=p[e]-p[s-1]
    return ans
def SumAllSubarraysOptimal(A):
    ans = 0
    n = len(A)
    for i in range(n):
        ans +=A[i]*(i+1)*(n-i)
    return ans
# A=[2,1,0,-6,8,3,2,4]
A = [1, 2, 3]
#A = [2, 1, 3]
#A=[ 2, 9, 5 ]
print(SumAllSubarrays(A))
print(SumAllSubarraysOptimal(A))