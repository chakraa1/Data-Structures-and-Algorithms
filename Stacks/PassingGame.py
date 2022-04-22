"""
====================
Problem Description
====================
There is a football event going on in your city. In this event, you are given A passes and players having ids between 1 and 106.
Initially, some player with a given id had the ball in his possession. You have to make a program to display the id of the player
who possessed the ball after exactly A passes.
There are two kinds of passes:
    1) ID
    2) 0

For the first kind of pass, the player in possession of the ball passes the ball "forward" to the player with id = ID.
For the second kind of pass, the player in possession of the ball passes the ball back to the player who had forwarded the ball to him.
In the second kind of pass "0" just means Back Pass.

Return the ID of the player who currently possesses the ball.

====================
Problem Constraints
====================
1 <= A <= 100000
1 <= B <= 100000

|C| = A

====================
Input Format
====================
The first argument of the input contains the number A.
The second argument of the input contains the number B ( id of the player possessing the ball in the very beginning).
The third argument is an array C of size A having (ID/0).

====================
Output Format
====================
Return the "ID" of the player who possesses the ball after A passes.

====================
Example Input
====================
Input 1:

 A = 10
 B = 23
 C = [86, 63, 60, 0, 47, 0, 99, 9, 0, 0]


Input 2:

 A = 1
 B = 1
 C = [2]

====================
Example Output
====================
Output 1: 63
Output 2: 2


====================
Example Explanation
====================
Explanation 1:

 Initially, Player having  id = 23  posses ball.
 After pass  1,  Player having  id = 86  posses ball.
 After pass  2,  Player having  id = 63  posses ball.
 After pass  3,  Player having  id = 60  posses ball.
 After pass  4,  Player having  id = 63  posses ball.
 After pass  5,  Player having  id = 47  posses ball.
 After pass  6,  Player having  id = 63  posses ball.
 After pass  7,  Player having  id = 99  posses ball.
 After pass  8,  Player having  id = 9   posses ball.
 After pass  9,  Player having  id = 99  posses ball.
 After pass  10, Player having  id = 63   posses ball.

Explanation 2: Ball is passed to 2.

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

def passing_game(A, B, C):
    ans = 0
    s = StackLL()
    s.push(B)
    for i in range(A):
        if C[i] != 0:
            s.push(C[i])
        else:
            s.pop()

    ans = s.peek()

    return ans


A = 10
B = 23
C = [86, 63, 60, 0, 47, 0, 99, 9, 0, 0]

A = 1
B = 1
C = [2]
print(passing_game(A, B, C))