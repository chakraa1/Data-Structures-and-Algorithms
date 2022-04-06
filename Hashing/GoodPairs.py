"""
Given an array of integers A and a number k,check if there is a pair of indexes (i,j) such that A[i] + A[j] = k .
Note (i,i) is valid pair
"""
def GoodPairs(A,K):
    ans = False
    pair_set = set()
    for x in A:
        if K - x in pair_set:
            return True
        else:
            pair_set.add(x)
    return ans

def GoodPairsCleaner(A,K):
    present = set(A)
    for x in A:
        if K - x in present:
            return True

    return False

"""
Challenge # 1 : What if (i, i) is not allowed?
"""
def GoodPairsWithoutII(A,K):
    present = set(A)
    for x in A:
        if x == K - x:
            counter = 0
            for y in A:
                if x == y:
                    counter += 1

            if counter >= 2:
                return True
        elif K - x in present:
            return True

    return False
"""
Challenge # 2 : Solve it in single pass?
"""

def GoodPairsSinglePass(A,K):
    present = set()
    for x in A:
        if K - x in present:
            return True
        present.add(x)

    return False


A = [2,8,4,-3,9,1,10,0,18,43,24]
K = 11
K = 7
K = 23
K = 21
"""
"""
print(GoodPairs(A,K))
print(GoodPairsCleaner(A,K))
print(GoodPairsSinglePass(A,K))
print(GoodPairsWithoutII(A,K))
print(GoodPairsSinglePass(A,K))