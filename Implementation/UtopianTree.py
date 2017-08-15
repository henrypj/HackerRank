#!/bin/python3

import sys

# The Utopian Tree goes through 2 cycles of growth every year. Each spring, 
# it doubles in height. Each summer, its height increases by 1 meter.

# Laura plants a Utopian Tree sapling with a height of 1 meter at the onset 
# of spring. How tall will her tree be after growth cycles?
# 
# Input Format
# 
# The first line contains an integer, T, the number of test cases. 
# T subsequent lines each contain an integer, N, denoting the number of cycles 
# for that test case.
#
# Constraints
#
# 1 <= T <= 10
# 0 <= N <= 60
# 
# Output Format
# 
# For each test case, print the height of the Utopian Tree after  cycles. 
# Each height must be printed on a new line.


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())

    Height = 1
    if n == 0:
        print(Height)
    else:
        for i in range(n):
            if i % 2 == 0:      # even so double
                Height *= 2
                else:           # odd, so add 1m
                Height += 1
        print(Height)
