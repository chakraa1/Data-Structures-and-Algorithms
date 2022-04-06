"""
Q2 - Subarray Distinct Count

Given an array of integers A and a number k,
find the number of distinct elements in every sub length K .


A = [1,2,1,3,4,5,1,2,3,4,1]
K = 5


"""
from collections import Counter
def SubarrayDistinctCount(A,K):
    ans = []
    n = len(A)
    for i in range(n - K + 1):
        distinct_elements = set()
        for j in range(i,i + K):
            distinct_elements.add(A[j])
        ans.append(len(distinct_elements))
    return ans

def SubarrayDistinctOptimized(A,K):
    ans = []
    n = len(A)
    counts = Counter()
    # Process the first window of size k
    for i in range(K):
        counts[A[i]] += 1
    ans.append(len(counts))

    # process the remaining windows
    for i in range(K,n):
        # increment the frequency of the last element of the new window
        counts[A[i]] += 1
        # decrement the frequency of the first element of the previous window
        to_remove = A[i-K]
        counts[to_remove] -= 1

        # if frequency drops to 0, remove the element
        if counts[to_remove] == 0:
            del counts[to_remove]

        ans.append(len(counts))

    return ans

A = [1,2,1,3,4,5,1,2,3,4,1]
K = 5
A = [4, 5, 1, 3, 1, 4, 6]
K = 3
print(SubarrayDistinctCount(A,K))
print(SubarrayDistinctOptimized(A,K))