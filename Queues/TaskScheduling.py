"""
====================
Problem Description
====================
A CPU has N tasks to be performed. It is to be noted that the tasks have to be completed in a specific order to avoid deadlock. In every clock cycle, the CPU can either perform a task or move it to the back of the queue.
You are given the current state of the scheduler queue in array A and the required order of the tasks in array B.
Determine the minimum number of clock cycles to complete all the tasks.

====================
Problem Constraints
====================
1 <= N <= 1000
1 <= A[i], B[i] <= N

====================
Input Format
====================
First argument consist of integer array A.
Second argument consist of integer array B.

====================
Output Format
====================
Return an integer denoting the minimum number of clock cycles required to complete all the tasks.

====================
Example Input
====================
Input 1:
A = [2, 3, 1, 5, 4]
B = [1, 3, 5, 4, 2]

Input 2:

A = [1]
B = [1]

====================
Example Output
====================
Output 1: 10
Output 2: 1

====================
Example Explanation
====================
Explanation 1:

According to the order array B task 1 has to be performed first, so the CPU will move tasks 2 and 3 to the end of the queue (in 2 clock cycles).
Total clock cycles till now = 2
Now CPU will perform task 1.
Total clock cycles till now = 3
Now, queue becomes [5, 4, 2, 3]
Now, CPU has to perform task 3. So it moves tasks 5, 4, and 2 to the back one-by-one.
Total clock cycles till now = 6
Now all the tasks in the queue are as in the required order so the CPU will perform them one-by-one.
Total clock cycles = 10

Explanation 2: Directly task 1 is completed.

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

def task_scheduling(A,B):
    min_clock_cycles = 0
    """
    A : current state of the scheduler queue 
    B : the required order of the tasks
    
    """
    current_state_sch_q = QueueLL()
    for i in range(len(A)):
        current_state_sch_q.Enqueue(A[i])

    i = 0
    n = len(B)
    while i < n:
        """
        Jobs order and schedule order NOT matched, hence moving it to the back of the queue 
        """
        while i < n and B[i] != current_state_sch_q.get_front():
            min_clock_cycles += 1
            current_state_sch_q.Enqueue(current_state_sch_q.get_front())
            current_state_sch_q.Dequeue()

        """
         Jobs order and schedule order MATCHED, hence can be considered as processed
        """
        current_state_sch_q.Dequeue()
        min_clock_cycles += 1

        i += 1

    return min_clock_cycles

A = [2, 3, 1, 5, 4]
B = [1, 3, 5, 4, 2]

"""
A = [1]
B = [1]

"""
print(task_scheduling(A,B))