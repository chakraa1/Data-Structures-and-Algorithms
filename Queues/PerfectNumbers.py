"""
Q1. Perfect Numbers

=====================
Problem Description
=====================
Given an integer A, you have to find the Ath Perfect Number.
A Perfect Number has the following properties:
It comprises only 1 and 2.
The number of digits in a Perfect number is even.
It is a palindrome number.

For example, 11, 22, 112211 are Perfect numbers, where 123, 121, 782, 1 are not.


=====================
Problem Constraints
=====================
1 <= A <= 100000

=====================
Input Format
=====================
The only argument given is an integer A.

=====================
Output Format
=====================
Return a string that denotes the Ath Perfect Number.

=====================
Example Input
=====================
Input 1: A = 2
Input 2: A = 3

=====================
Example Output
=====================
Output 1: 22
Output 2: 1111


=====================
Example Explanation
=====================
Explanation 1:

First four perfect numbers are:
1. 11
2. 22
3. 1111
4. 1221
Explanation 2:

First four perfect numbers are:
1. 11
2. 22
3. 1111
4. 1221

"""
class LinkedListNode:
    def __init__(self,x):
        self.data = x
        self.next = None


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
def PerfectNumbers(A):
    q = QueueLL()

    q.Enqueue(1)
    q.Enqueue(2)

    cnt = 1

    while True:
       """
       Step 1 - Pop from left 
       """
       x = str(q.Dequeue())

       """
       Step 2 - create answer 
       """
       ans = x + x[::-1]
       if cnt == A:
           break

       """
        Step 3 - create answer 
       """
       q.Enqueue(int(x + '1'))
       q.Enqueue(int(x + '2'))

       cnt += 1


    return ans

A = 5

print(PerfectNumbers(A))