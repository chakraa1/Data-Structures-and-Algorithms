"""
====================
Problem Description
====================
You are given an integer T (Number of test cases). For each test case, You are given two sorted arrays A and B.
You have to merge the given arrays into a single sorted array.


====================
Problem Constraints
====================
1 <= T <= 10
1 <= n1, n2 <= 105
-109 <= A[i], B[i] <= 109

====================
Input Format
====================
First line of the input contains a single integer T.

Next, each of the test case consists of 4 lines:

First line consists integer is an integer n1 denoting the length of array A
Second line consists of n1 elements of array A
Third line consists integer is an integer n2 denoting the length of array B
Fourth line consists of n2 elements of array B

====================
Output Format
====================
For each test case, return a sorted integer array having length n1 + n2.

====================
Example Input
====================
Input 1:

 1
 3
 -1 2 4
 5
 -1 -1 1 3 5

Input 2:

 1
 1
 1
 4
 2 3 4 5

====================
Example Output
====================
Output 1:

 -1 -1 -1 1 2 3 4 5
Output 2:

 1 2 3 4 5

====================
Example Explanation
====================
Explanation 1:

 Each element in Sorted array [-1, -1, -1, 1, 2, 3, 4, 5] comes either from A or B.
Explanation 2:

 Each element in Sorted array [1, 2, 3, 4, 5] comes either from A or B.

"""


def merge():
    ans = None
    # YOUR CODE GOES HERE
    print("Please test cases (T) : ",end ="")
    T = int(input())
    print("Number of test cases (T) : ",T)
    while T > 0:
        print("Please enter n1 : ",end ="")
        n1 = int(input())
        print("n1 --> ",n1)
        print("Please enter A : ", end="")
        A = list(map(int, input().split()))
        print("A --> ", A)
        print("Please enter n2 : ", end="")
        n2 = int(input())
        print("n2 --> ", n2)
        print("Please enter A : ", end="")
        B = list(map(int, input().split()))
        print("B --> ", B)

        # YOUR CODE GOES HERE
        a = 0
        b = 0
        k = 0

        ans = [0] * (n1 + n2)

        while a < n1 and b < n2:
            if A[a] > B[b]:
                ans[k] = B[b]
                b += 1
                k += 1
            else:
                ans[k] = A[a]
                a += 1
                k += 1

        while a < n1:
            ans[k] = A[a]
            k += 1
            a += 1

        while b < n2:
            ans[k] = B[b]
            k += 1
            b += 1

        T -= 1

    return ans
print(merge())