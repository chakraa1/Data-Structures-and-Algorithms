"""
======================
Problem Description
======================
Given an array of integers A and an integer B, we need to reverse the order of the first B elements of the array, leaving the other elements in the same relative order.

NOTE: You are required to the first insert elements into an auxiliary queue then perform Reversal of first B elements.


======================
Problem Constraints
======================
1 <= B <= length of the array <= 500000
1 <= A[i] <= 100000


======================
Input Format
======================
The argument given is the integer array A and an integer B.


======================
Output Format
======================
Return an array of integer after reversing the first B elements of A using queue.


======================
Example Input
======================
Input 1:

 A = [1, 2, 3, 4, 5]
 B = 3
Input 2:

 A = [5, 17, 100, 11]
 B = 2

======================
Example Output
======================
Output 1:

 [3, 2, 1, 4, 5]
Output 2:

 [17, 5, 100, 11]


======================
Example Explanation
======================
Explanation 1:

 Reverse first 3 elements so the array becomes [3, 2, 1, 4, 5]
Explanation 2:

 Reverse first 2 elements so the array becomes [17, 5, 100, 11]

"""

class LinkedListNode:
    def __init__(self,x):
        self.data = x
        self.next = None


class StackLL:
    def __init__(self):
        self.top = -1
        self.size = 0
        self.head = None


    def push(self,x):
        new_node = LinkedListNode(x)
        new_node.next = self.head
        self.head = new_node
        self.top = self.head
        self.size += 1


    def pop(self):
        if self.head != None:
            self.head = self.head.next
            self.top = self.head
            self.size -= 1

    def isEmpty(self):
        if self.size == 0:
            return True
        return False

    def peek(self):
        if self.head != None:
            return self.head.data
        return None

    def stack_size(self):
        return self.size

    def print_stack(self):
        itr = self.head
        while itr != None:
            print(itr.data,end =" ")
            itr = itr.next
        print()

def reversing_elements(A,B):
    result = []
    my_stack = StackLL()
    for i in range(B):
        my_stack.push(A[i])


    for i in range(my_stack.size):
        result.append(my_stack.peek())
        my_stack.pop()

    for j in range(B,len(A)):
        result.append(A[j])

    return result

A = [1, 2, 3, 4, 5]
B = 3
print(reversing_elements(A,B))
