"""
Stack Implementation
1. push()
2. pop()
3. top/peek()
4. isEmpty()
5. size()

"""
"""
Using fixed size array
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

my_stack = StackLL()
my_stack.push(2)
my_stack.push(5)
my_stack.push(1)
my_stack.print_stack()
print("Top value--> ",my_stack.peek())
print("size --> ",my_stack.stack_size())
my_stack.pop()
print("Top value--> ",my_stack.peek())
print("size --> ",my_stack.stack_size())


