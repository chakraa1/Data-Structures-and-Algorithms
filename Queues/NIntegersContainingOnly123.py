"""
========================
Problem Description
========================
Given an integer, A. Find and Return first positive A integers in ascending order containing only digits 1, 2, and 3.
NOTE: All the A integers will fit in 32-bit integers.

========================
Problem Constraints
========================
1 <= A <= 29500

========================
Input Format
========================
The only argument given is integer A.

========================
Output Format
========================
Return an integer array denoting the first positive A integers in ascending order containing only digits 1, 2 and 3.


========================
Example Input
========================
Input 1: A = 3
Input 2: A = 7

========================
Example Output
========================
Output 1: [1, 2, 3]
Output 2: [1, 2, 3, 11, 12, 13, 21]


========================
Example Explanation
========================
Explanation 1: Output denotes the first 3 integers that contains only digits 1, 2 and 3.
Explanation 2: Output denotes the first 3 integers that contains only digits 1, 2 and 3.

"""
class LinkedListNode:
    def __init__(self,x):
        self.data = x
        self.next = None


class QueueLL:
    def __init__(self):
        self.size = 0
        self.head = None
        self.tail = None


    def Enqueue(self,x):
        new_node = LinkedListNode(x)
        if self.head == None:
            self.tail = new_node
            self.head = new_node
        else:
            self.tail.next = new_node
            self.tail = self.tail.next

        self.size += 1

    def Dequeue(self):
        if self.head != None:
            dq_element = self.head.data
            self.head = self.head.next
            self.size -= 1
            return dq_element
        else:
            self.tail = None
            self.size = 0

        return None

    def print_queue(self):
        itr = self.head
        while itr != None:
            print(itr.data,end =" ")
            itr = itr.next
        print()

def NIntegersContainingOnly123(A):
    results = []
    q = QueueLL()
    q.Enqueue(1)
    q.Enqueue(2)
    q.Enqueue(3)

    if A <= 3:
        for i in range():
            results.append(i)
        return results
    else:
        results.extend([1,2,3])
        A = A - 3
        while A > 0:
            element = q.Dequeue()
            if A > 0:
                num_1 = (element * 10) + 1
                results.append(num_1)
                q.Enqueue(num_1)
                A -= 1
            else:
                break

            if A > 0:
                num_2 = (element * 10) + 2
                results.append(num_2)
                q.Enqueue(num_2)
                A -= 1
            else:
                break

            if A > 0:
                num_3 = (element * 10) + 3
                results.append(num_3)
                q.Enqueue(num_3)
                A -= 1
            else:
                break

        return results

A = 2
A = 7
print(NIntegersContainingOnly123(A))