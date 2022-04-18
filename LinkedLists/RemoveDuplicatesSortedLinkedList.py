"""
======================
Problem Description
======================
Given a sorted linked list, delete all duplicates such that each element appears only once.

======================
Problem Constraints
======================
0 <= length of linked list <= 106

======================
Input Format
======================
First argument is the head pointer of the linked list.

======================
Output Format
======================
Return the head pointer of the linked list after removing all duplicates.

======================
Example Input
======================
Input 1: 1->1->2
Input 2: 1->1->2->3->3

======================
Example Output
======================
Output 1: 1->2
Output 2: 1->2->3

======================
Example Explanation
======================
Explanation 1: Each element appear only once in 1->2
"""
class ListNode:
    def __init__(self, x):
        self.data = x
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


    def print_all(self):
        curr_position = self.head
        if curr_position == None:
            return
        else:
            print(curr_position.data, end="")
            curr_position = curr_position.next
            while curr_position != None:
                print("", end=" ")
                print(curr_position.data, end="")
                curr_position = curr_position.next
        print()

ll = LinkedList()
ll.insert_node(22,1)
ll.insert_node(22,2)
ll.insert_node(23,3)
ll.insert_node(24,4)
ll.insert_node(25,5)
ll.insert_node(25,6)
ll.print_all()
def deleteDuplicates(A):
    def deleteDuplicates(self, A):
        curr = A

        while A != None:
            while A.next != None and A.val == A.next.val:
            # if A.next != None and A.val == A.next.val: # why this will not work
                A.next = A.next.next
            A = A.next

        return curr
deleteDuplicates(ll.head)
