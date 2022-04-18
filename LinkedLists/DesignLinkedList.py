"""
=====================
Problem Description
=====================
Given a matrix A of size Nx3 representing operations. Your task is to design the linked list based on these operations.
There are four types of operations:
    0 x -1: Add a node of value x before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.

    1 x -1: Append a node of value x to the last element of the linked list.

    2 x index: Add a node of value x before the indexth node in the linked list. If the index equals the length of the linked list, the node will be appended to the end of the linked list. If the index is greater than the length, the node will not be inserted.

    3 index -1: Delete the indexth node in the linked list, if the index is valid.

A[i][0] represents the type of operation.
A[i][1], A[i][2] represents the corresponding elements with respect to type of operation.

Note: Indexing is 0 based.

=====================
Problem Constraints
=====================
1 <= Number of operations <= 1000
1 <= All node values <= 109

=====================
Input Format
=====================
The only argument given is matrix A.

=====================
Output Format
=====================
Return the pointer to the starting of the linked list.

=====================
Example Input
=====================
Input 1:

A = [[0, 1, -1],
     [1, 2, -1],
     [2, 3, 1]]

Input 2:

A = [[0, 1, -1],
     [1, 2, -1],
     [2, 3, 1],
     [0, 4, -1],
     [3, 1, -1],
     [3, 2, -1]]

=====================
Example Output
=====================
Output 1:
1 -> 3 -> 2 -> NULL

=====================
Output 2:
=====================
4 -> 3 -> NULL

=====================
Example Explanation
=====================
Explanation 1:

After first operation the list is 1 -> NULL
After second operation the list is 1 -> 2 -> NULL
After third operation the list is 1 -> 3 -> 2 -> NULL

Explanation 2:

After first operation the list is 1 -> NULL
After second operation the list is 1 -> 2 -> NULL
After third operation the list is 1 -> 3 -> 2 -> NULL
After fourth operation the list is 4 -> 1 -> 3 -> 2 -> NULL
After fifth operation the list is 4 -> 3 -> 2 -> NULL
After sixth operation the list is 4 -> 3 -> NULL

"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def findNodeByPosition(self,position):
        current_node = self.head
        while current_node != None and position > 0:
            current_node = current_node.next
            position -= 1
        if current_node == None:
            return None
        return current_node

    def insert_at_head_position(self,value):
        new_node = ListNode(value)
        if self.head == None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def insert_at_tail_position(self,value):
        new_node = ListNode(value)
        if self.head == None:
            self.head = new_node
            return
        current_position = self.head
        while current_position.next != None:
            current_position = current_position.next
        current_position.next = new_node

    def insert_at_given_position(self,value,position):
        target_position = self.findNodeByPosition(position-2)
        if target_position == None:
            return
        else:
            new_node = ListNode(value)
            new_node.next = target_position.next
            target_position.next = new_node


    def insert_node(self, value, position=None):
        node = ListNode(value)
        if position == None:
            self.insert_at_tail_position(value)
        elif position == 1:
            self.insert_at_head_position(value)
        else:
            self.insert_at_given_position(value, position)

    def delete_at_position(self,position):
        if position == 1:
            if self.head != None:
                self.head = self.head.next
        else:
            current_position = self.findNodeByPosition(position - 2)
            if current_position == None:
                return
            else:
                if current_position.next != None:
                    current_position.next = current_position.next.next

class Solution:
    # @param A : list of list of integers
    # @return the head node in the linked list
    def solve(self, A):
        """
            A[i][0] represents the type of operation.
            A[i][1], A[i][2] represents the corresponding elements with respect to type of operation.

            0 x -1:     ADD a node of value x BEFORE the FIRST element of the linked list
            1 x -1:     APPEND a node of value x AFTER the LAST element of the linked list.
            2 x index:  ADD a node of value x BEFORE the indexth node in the linked list . If the index equals the length
                        of the linked list, the node will be appended to the end of the linked list.
                        If the index is greater than the length, the node will not be inserted.

            3 index -1: DELETE the indexth node in the linked list, if the index is valid.

            ======
            Input
            ======
            A = [[0, 1, -1],
                [1, 2, -1],
                [2, 3, 1]]

            =============
            Explanation
            =============

            [0, 1, -1] - > Add a node of value 1 BEFORE the 1st element    --> After first operation the list is 1 -> NULL
            [1, 2, -1] - > Append a node of value 2 AFTER the last element --> After second operation the list is 1 -> 2 -> NULL
            [2, 3, 1]  - > Add a node of value 3 BEFORE 3rd index position --> After third operation the list is 1 -> 3 -> 2 -> NULL
        """
        for row in range(len(A)):
            type_of_operation = A[row][0]
            x = 0
            if type_of_operation in (0,1,2):
                x = A[row][1]

            if type_of_operation == 2:
                index = A[row][2]
            elif type_of_operation == 3:
                index = A[row][1]





