"""
====================
Problem Description
====================
Design and implement a Linked List data structure.
A node in a linked list should have the following attributes - an integer value and a pointer to the next node.

It should support the following operations:

    insert_node(position, value) - To insert the input value at the given position in the linked list.
    delete_node(position) - Delete the value at the given position from the linked list.
    print_ll() - Print the entire linked list, such that each element is followed by a single space.

====================
Note:
====================

If an input position does not satisfy the constraint, no action is required.
Each print query has to be executed in a new line.

====================
Problem Constraints
====================
1 <= position <= n where, n is the size of the linked-list.

====================
Input Format
====================
First line contains an integer denoting number of cases, let's say t.
Next t line denotes the cases.

====================
Output Format
====================
When there is a case of print_ll(),  Print the entire linked list, such that each element is followed by a single space.
NOTE: You don't need to return anything.

====================
Example Input
====================
5
i 1 23
i 2 24
p
d 1
p

====================
Example Output
====================
23 24
24

====================
Example Explanation
====================
After first two cases linked list contains two elements 23 and 24.
At third case print: 23 24.
At fourth case delete value at first position, only one element left 24.
At fifth case print: 24.

"""

class Node:
    def __init__(self,value):
        self.data = value
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
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def insert_at_tail_position(self,value):
        new_node = Node(value)
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
            new_node = Node(value)
            new_node.next = target_position.next
            target_position.next = new_node


    def insert_node(self, value, position=None):
        node = Node(value)
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
def insert_node(position, value):
    # @param position, an integer
    # @param value, an integer
    ll.insert_node(value,position)
def delete_node(position):
    # @param position, integer
    # @return an integer
    ll.delete_at_position(position)
def print_ll():
    # Output each element followed by a space
    ll.print_all()