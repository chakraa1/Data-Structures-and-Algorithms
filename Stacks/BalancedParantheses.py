"""
===================
Problem Description
===================
Given a string A consisting only of '(' and ')'.
You need to find whether parentheses in A are balanced or not, if it is balanced then return 1 else return 0.

===================
Problem Constraints
===================
1 <= |A| <= 105

===================
Input Format
===================
First argument is an string A.

===================
Output Format
===================
Return 1 if parantheses in string are balanced else return 0.

===================
Example Input
===================
Input 1: A = "(()())"
Input 2: A = "(()"

===================
Example Output
===================
Output 1: 1
Output 2: 0

===================
Example Explanation
===================
Explanation 1: Given string is balanced so we return 1.
Explanation 2: Given string is not balanced so we return 0.

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

def balanced_parantheses(A):
    ans = 0
    s = StackLL()

    if "(" not in A or ")" not in A:
        return 0

    for paran in A:
        if paran == "(":
            s.push("(")
        elif paran == ")" and s.isEmpty():
            return 0
        else:
            s.pop()

    if s.isEmpty():
        ans = 1

    return ans

A = "(()())"
#A = "(()"
A= ")))"
print(balanced_parantheses(A))