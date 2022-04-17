"""
====================
Problem Description
====================
Given a linked list of integers, find and return the middle element of the linked list.
NOTE: If there are N nodes in the linked list and N is even then return the (N/2 + 1)th element.

====================
Problem Constraints
====================
1 <= length of the linked list <= 100000
1 <= Node value <= 109

====================
Input Format
====================
The only argument given head pointer of linked list.

====================
Output Format
====================
Return the middle element of the linked list.

====================
Example Input
====================
Input 1: 1 -> 2 -> 3 -> 4 -> 5
Input 2: 1 -> 5 -> 6 -> 2 -> 3 -> 4

====================
Example Output
====================
Output 1: 3
Output 2: 2

====================
Example Explanation
====================
Explanation 1: The middle element is 3.
Explanation 2: The middle element in even length linked list of length N is ((N/2) + 1)th element which is 2.

"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def solve(A):
    current_node = A
    ll_size = 0
    while current_node != None:
        current_node = current_node.next
        ll_size += 1

    target_node_position = 0
    if ll_size % 2 != 0:
        target_node_position = ll_size // 2
    else:
        target_node_position = (ll_size // 2) + 1

    current_node = A
    while current_node != None and target_node_position > 0:
        current_node = current_node.next
        ll_size += 1

    return current_node.data

def solve2(A):
    slow_pointer = A
    fast_pointer = A

    while fast_pointer != None and fast_pointer.next != None:
        slow_pointer = slow_pointer.next
        fast_pointer = fast_pointer.next.next

    return slow_pointer.val


A = [ 46,76,35 ]
print(solve(A))
