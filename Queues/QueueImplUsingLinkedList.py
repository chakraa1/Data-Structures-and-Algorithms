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
            self.head = self.head.next
            self.size -= 1
        else:
            self.tail = None
            self.size = 0

    def isEmpty(self):
        if self.size == 0:
            return True
        return False

    def get_front(self):
        if self.head != None:
            return self.head.data
        return None

    def queue_size(self):
        return self.size

    def print_queue(self):
        itr = self.head
        while itr != None:
            print(itr.data,end =" ")
            itr = itr.next
        print()

my_queue = QueueLL()
my_queue.Enqueue(2)
my_queue.Enqueue(5)
my_queue.Enqueue(1)
my_queue.print_queue()
print("front value--> ",my_queue.get_front())
print("size --> ",my_queue.queue_size())
my_queue.Dequeue()
print("front value--> ",my_queue.get_front())
print("size --> ",my_queue.queue_size())

my_queue.print_queue()


