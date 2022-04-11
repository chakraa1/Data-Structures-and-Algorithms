"""
======================
Problem Description
======================
Write a recursive function that, given a string S, prints the characters of S in reverse order.

======================
Problem Constraints
======================
1 <= |s| <= 1000

======================
Input Format
======================
First line of input contains a string S.

======================
Output Format
======================
Print the character of the string S in reverse order.

======================
Example Input
======================

Input 1: scaleracademy
Input 2: cool

======================
Example Output
======================
Output 1:ymedacarelacs
Output 2: looc

======================
Example Explanation
======================
Explanation 1: Print the reverse of the string in a single line.

"""

import sys
sys.setrecursionlimit(1000000)
def main(A):
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output

    if len(A) == 0:
        return
    else:
        main(A[1:])
        print(A[0],end ="")


if __name__ == '__main__':
    A = input()
    main(A)