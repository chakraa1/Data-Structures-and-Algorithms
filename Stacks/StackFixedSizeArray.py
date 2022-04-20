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

class Stack:
    def __init__(self):
        self.top = -1
        self.size = 0
        self.max_fixed_size = 10
        self.stack = [None] * self.max_fixed_size


    def push(self,x):
        if self.top + 1 < self.max_fixed_size:
            self.top += 1
            self.stack[self.top] = x
            self.size += 1


    def pop(self,x):
        if self.top >= 0:
            self.top -= 1
            self.size -= 1

    def isEmpty(self):
        if self.size == 0 or self.top == -1:
            return True
        return False

    def peek(self):
        if self.top >= 0 and self.top < self.max_fixed_size:
            return self.stack[self.top]

        return None

    def stack_size(self):
        return self.size

    def print_stack(self):
        print(self.stack)

my_stack = Stack()
my_stack.push(2)
my_stack.push(5)
my_stack.push(1)
my_stack.print_stack()
print("Top value--> ",my_stack.peek())
print("size --> ",my_stack.stack_size())
my_stack.pop(1)
print("Top value--> ",my_stack.peek())
print("size --> ",my_stack.stack_size())


