#!/bin/python3
import sys
"""
# Description
# Difficulty: Easy
# 
# Bob has a strange counter. At the first second, t=1, it displays the number 3.
# At each subsequent second, the number displayed by the counter decrements by 1.
#
# The counter counts down in cycles. In the second after the counter counts down
# to 1, the number becomes 2x the initial number for that countdown cycle and 
# then continues counting down from the new initial number in a new cycle. The 
# diagram below shows the counter values for each time t in the first three cycles:
#
# time value     time value     time value       time value
# +---+---+      +---+---+      +----+----+      +----+----+
# | 1 | 3 |      | 4 | 6 |      | 10 | 12 |      | 22 | 24 |
# +---+---+      +---+---+      +----+----+      +----+----+
# | 2 | 2 |      | 5 | 5 |      | 11 | 11 |      | 23 | 23 |
# +---+---+      +---+---+      +----+----+      +----+----+
# | 3 | 1 |      | 6 | 4 |      | 12 | 10 |      | 24 | 22 |
# +---+---+      +---+---+      +----+----+      +----+----+
#                | 7 | 3 |      | 13 |  9 |      | 25 | 21 |
#                +---+---+      +----+----+      +----+----+
#                | 8 | 2 |      | 14 |  8 |      | 26 | 20 |
#                +---+---+      +----+----+      +----+----+
#                | 9 | 1 |      | 15 |  7 |      | 27 | 19 |
#                +---+---+      +----+----+      +----+----+
#                    +3         | ...| ...|      | ...| ...|
#                               +----+----+      +----+----+
#                               | 21 |  1 |      | 45 |  1 |
#                               +----+----+      +----+----+
#                                    +6              +18
#
# Given a time, t, find and print the value displayed by the counter at time t.
#
# Input Format
#
# A single integer denoting the value of t.
#
# Constraints
#
# 1 <= t <= 10**12
# 1 <= t <= 10**5 for 60% of the maximum score.
#
# Output Format 
#
# Print the value displayed by the strange counter at the given time t.
#
# Example 0
#
# Given Input:
# 4
#
# Output:
# 6
#
# Explanation:
# Time t=4 marks the beginning of the second cycle in which the counter displays
# a number that is double the initial number displayed at the beginning of the 
# previous cycle (i.e., 2 x 3 = 6). This is also shown in the diagram in the 
# Problem Statement above.
#
# Solution:
#    
# The solution below is from the discussion board, very elegant.
#
# t = int(input().strip())
# rem = 3
# while t > rem:
#     t -= rem
#     rem *= 2
# print(rem-t+1)
#
# Here is another...
#
# from math import *
# t = int(input().strip())
# s = int(log2((t-1)//3+1))
# a,b=3*(2**s-1)+1,3*2**s
# print(a+b-t) 
"""
# My Solution

from bisect import bisect
t = int(input().strip())
counter = []
startNum = 1
startVal = 3
for i in range(1000):
    counter.append(startNum)
    startNum += startVal
    startVal *= 2

val = counter[bisect(counter, t) - 1] * 2 + 2
print(val - t)    
