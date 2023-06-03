"""
Leet code # 11 - https://leetcode.com/problems/container-with-most-water/
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.
A[i] = Height of each wall

==============================
Table calculation for logic
==============================
p1 p2 Height(A[p2]-A[p1]) width = p2-p1 Area [Max_water]

Logic - Smaller height should be always moved 

Difficulty Level : Medium
Time complexity: O(n)
Space complexity: O(1)
"""

def max_water(A):

    return max_water

A = [3,7,4,5,2]
print(max_water(A))