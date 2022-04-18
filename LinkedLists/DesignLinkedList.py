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


def print_ll(head):
    itr = head
    while itr != None:
        print(itr.val, end=" ")
        itr = itr.next
    print()

def AddNodeBeforeFirstElement(head, value):
    new_node = ListNode(value)
    new_node.next = head
    head = new_node
    return head


def AppendNodeAfterLastElement(head, value):
    if head == None:
        head = ListNode(value)
    else:
        new_node = ListNode(value)
        current_head = head
        while current_head.next != None:
            current_head = current_head.next

        current_head.next = new_node

    return head


def AddNodeBeforeGivenIndex(head, value, index):
    if index == 0:
        return AddNodeBeforeFirstElement(head, value)
    else:
        new_node = ListNode(value)
        current_head = head

        while current_head != None and index - 1 > 0:
            current_head = current_head.next
            index -= 1
        """
         When given index is out of range of existing linked list
        """
        if current_head == None:
            return head
        else:
            new_node.next = current_head.next
            current_head.next = new_node

            return head


def DeleteNodeGivenIndex(head, index):
    if head == None:
        return head
    if index == 0:
        return head.next
    else:

        current_head = head

        while current_head != None and index - 1 > 0:
            current_head = current_head.next
            index -= 1

        """
        When given index is out of range of existing linked list
        
        """
        if current_head == None or current_head.next == None:
            return head
        else:
            current_head.next = current_head.next.next
            return head

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
        head = None

        for row in range(len(A)):

            type_of_operation = A[row][0]
            # print(type_of_operation, A[row][1], A[row][2])

            if type_of_operation == 0:
                head = AddNodeBeforeFirstElement(head, A[row][1])
            elif type_of_operation == 1:
                head = AppendNodeAfterLastElement(head, A[row][1])
            elif type_of_operation == 2:
                head = AddNodeBeforeGivenIndex(head, A[row][1], A[row][2])
            else:
                head = DeleteNodeGivenIndex(head, A[row][1])

            # print_ll(head)

        return head


