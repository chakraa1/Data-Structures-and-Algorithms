def reverse(A,start_index,end_index):
    while (start_index <= end_index):
        A[start_index],A[end_index]=A[end_index],A[start_index]
        start_index += 1
        end_index -= 1
    return A
A = [1, 2, 3, 4, 5]
n = len(A)
#print("Original",A)
#print("Reversed",reverse(A,0,n-1))

def rotate_by_d_index(A,d):
    n = len(A)
    A = reverse(A,0,n-1)
    A = reverse(A,0,d-1)
    A = reverse(A, d, n-1)

    return A
print("Original",A)
print("After rotation from D index",rotate_by_d_index(A,3))


