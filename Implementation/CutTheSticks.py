#!/bin/python3

import sys
"""
# You are given N sticks, where the length of each stick is a positive integer.
# A cut operation is performed on the sticks such that all of them are reduced
# by the length of the smallest stick.
#
# Suppose we have six sticks of the following lengths:
# 5 4 4 2 2 8
#
# Then, in one cut operation we make a cut of length 2 from each of the six 
# sticks. For the next cut operation four sticks are left (of non-zero length),
# whose lengths are the following:
#
# 3 2 2 6
#
# The above step is repeated until no sticks are left.
#
# Given the length of N sticks, print the number of sticks that are left before
# each subsequent cut operations.
#
# Note: For each cut operation, you have to recalcuate the length of smallest
# sticks (excluding zero-length sticks).
#
# Input Frmat
#
# The first line contains a single integer N. 
# The next line contains N integers: a0, a1,...aN-1 separated by space, where
# a(i) represents the length of the i'th stick. 
#
# Constraints
#
# 1 <=  N   <= 1000
# 1 <= a(i) <= 1000
#
# Output Format 
#
# For each operation, print the number of sticks that are cut, on separate lines.
#
# Example 1
#
# Given Input:
# 6
# 5 4 4 2 2 8
#
# Output:
# 6
# 4
# 2
# 1
#
# Explanation:
# sticks-length        length-of-cut   sticks-cut
# 5 4 4 2 2 8             2               6
# 3 2 2 _ _ 6             2               4
# 1 _ _ _ _ 4             1               2
# _ _ _ _ _ 3             3               1
# _ _ _ _ _ _           DONE            DONE#
#
# Example 2
#
# Given Input:
# 8
# 1 2 3 4 3 3 2 1
#
# Output:
# 8
# 6
# 4
# 1
#
# Explanation:
# sticks-length         length-of-cut   sticks-cut
# 1 2 3 4 3 3 2 1         1               8
# _ 1 2 3 2 2 1 _         1               6
# _ _ 1 2 1 1 _ _         1               4
# _ _ _ 1 _ _ _ _         1               1
# _ _ _ _ _ _ _ _       DONE            DONE
#
# Solution
# 
"""

n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

#while sum(i > 0 for i in arr) >= 1:
while max(arr) > 0:
    numCuts = 0
    minVal = min(x for x in arr if x > 0)
    for j in range(len(arr)):
        if arr[j] > 0:
            arr[j] -= minVal
            numCuts += 1
    print(numCuts)
