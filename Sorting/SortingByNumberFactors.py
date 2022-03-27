"""
Sort an array by Numbers of factors
"""
from functools import cmp_to_key
def countFactors(N):
    i = 1
    cnt = 0
    while i*i < N:
        if N % i == 0:
            if i * i == N:
                cnt += 1
            else:
                cnt += 2
        i += 1
    return cnt
"""
Sorting by factor count DESC and if same factor count then sort the element values by values ASC
"""
def compare_by_factor(a,b):
    a_fcnt = countFactors(a) # O(sqrt(a)) --> Expensive operation
    b_fcnt = countFactors(b) # O(sqrt(b)) --> Expensive operation

    if a_fcnt < b_fcnt:
        return 1        # desc
    elif a_fcnt > b_fcnt:
        return -1
    else:
        if a < b:
            return -1   # asc
        elif a == b:
            return 0
        else:
            return 1


"""
Initializing Inputs 
"""
A = [1,2,5,10,15,16,6]
print("before sorting --> ",A)

"""
Approach 1 -  Comparator "cmp-to-key" approach
              Time complexity - nlogn * (sqrt(a) + sqrt(b)) (i.e. assume this to be very expensive if array
                                                            value is large . we'll call it as x
"""
print("after sorting approach 1 --> ",sorted(A,key=cmp_to_key(compare_by_factor)))

"""
Approach 2 -  Exploit stability
Time complexity - N * x + nlogn * 1 (why 1 as we're comparing only two values )
Optimized approach than approach 1
Pros - Time complexity is batter than approach 1 
Cons - Space complexity is more as we're storing keys arrays and then applying sort 
"""
# First sort by value ascending
A_sorted_asc=sorted(A)
# Next step - sort by number of factors desc
result = sorted(A_sorted_asc,key=countFactors,reverse=True)
print("after sorting approach 2 --> ", result)

"""
Approach 3 -  Tuple comparison  
"""
def custom_key(N):
    return -countFactors(N), N

# (1 , 2) < (1 , 3) ---> True, as it's comparing tuples lexicographically
# (1 , 2) > (2 , 1 ) ----> False
print("after sorting approach 3 --> ", sorted(A,key=custom_key))
# Alternative syntax to above tuple comparison using lamda function
print("after sorting approach 3.1 --> ", sorted(A, key=lambda n: (-countFactors(n), n)))





