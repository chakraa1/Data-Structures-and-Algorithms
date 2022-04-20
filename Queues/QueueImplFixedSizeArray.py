"""
Queue Implementation
1. Enqueue()
2. Dequeue()
3. front()
4. isEmpty()
5. size()

"""
"""
Using fixed size array
"""

class Queue:
    def __init__(self):
        self.front = -1
        self.rear = -1
        self.size = 0
        self.max_fixed_size = 10
        self.queue = [None] * self.max_fixed_size


    def Enqueue(self,x):
        if self.front + 1 < self.max_fixed_size:
            self.front += 1
            self.rear += 1
            self.queue[self.rear] = x
            self.size += 1

            if self.rear == 0:
                self.front = 0


    def Dequeue(self,x):
        if self.front >= 0:
            self.queue[self.front] = None
            self.front += 1
            self.size -= 1


    def isEmpty(self):
        if self.size == 0:
            return True
        return False

    def get_front(self):
        if self.front >= 0:
            return self.queue[self.front]

        return None

    def queue_size(self):
        return self.size

    def print_queue(self):
        print(self.queue)

my_queue = Queue()
my_queue.Enqueue(2)
my_queue.Enqueue(5)
my_queue.Enqueue(1)
my_queue.print_queue()
print("Front value--> ",my_queue.get_front())
print("size --> ",my_queue.queue_size())
my_queue.Dequeue(1)
print("size --> ",my_queue.queue_size())
my_queue.print_queue()


