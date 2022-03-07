def solve(A):
    ps_even=[A[0]]
    for i in range(1,len(A)):
        if i%2==0:
            ps_even.append(A[i]+ps_even[i-1])
        else:
            ps_even.append(0+ps_even[i-1])
    print(ps_even)

    ps_odd = [0]
    for i in range(1, len(A)):
        if i % 2 != 0:
            ps_odd.append(A[i] + ps_odd[i - 1])
        else:
            ps_odd.append(0 + ps_odd[i - 1])
    print(ps_odd)

    n=len(A)
    count=0
    for i in range(len(A)):
        sum_of_even_elements_after_i=ps_even[n-1]-ps_even[i]
        sum_of_odd_elements_after_i=ps_odd[n-1]-ps_odd[i]
        if i==0 and sum_of_even_elements_after_i == sum_of_odd_elements_after_i:
            count +=1
        else:
            sum_of_even_elements_before_i = ps_even[i-1]
            sum_of_odd_elements_before_i = ps_odd[i-1]

            if sum_of_even_elements_before_i+sum_of_odd_elements_after_i == sum_of_odd_elements_before_i+sum_of_even_elements_after_i:
                count +=1

    return count
#A=[ -1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15, -16, -17, -18, -19, -20, -21, -22, -23, -24, -25, -26, -27, -28, -29, -30, -31, -32, -33, -34, 69, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34 ]
A=[2, 1, 6, 4]
#A=[1,1,1]
print(solve(A))


