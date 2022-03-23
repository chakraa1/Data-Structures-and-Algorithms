"""
There are 100 doors, all closed. In a nearby cage are 100 monkeys.
The first monkey is let out and runs along the doors opening every one.
The second monkey is then let out and runs along the doors closing the 2nd, 4th, 6th,… - all the even-numbered doors.
The third monkey is let out. He attends only to the 3rd, 6th, 9th,… doors (every third door, in other words),
closing any that is open and opening any that is closed, and so on.
After all 100 monkeys have done their work in this way, what state are the doors in after the last pass?

Please find the number of open doors.

"""
import math


def OpenDoors(N):
    """
    Only perfect squares has odd number of factors. Every other number has even factors
    Hence number of open doors would be a perfect square of the input number  
    """
    return math.sqrt(N)
N = 100
print(OpenDoors(N))