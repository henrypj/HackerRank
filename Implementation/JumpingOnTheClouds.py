#!/bin/python3

import sys
"""
# Emma is playing a new mobile game involving n clouds numbered from 0 to n-1. 
# A player initially starts out on cloud c(0), and they must jump to cloud c(n-1). 
# In each step, she can jump from any cloud i to cloud i+1 or cloud i+2.
#
# There are two types of clouds, ordinary clouds and thunderclouds. The game 
# ends if Emma jumps onto a thundercloud, but if she reaches the last cloud 
# (i.e., c(n-1)), she wins the game!
#
# Can you find the minimum number of jumps Emma must make to win the game? 
# It is guaranteed that clouds c(0) and c(n-1) are ordinary-clouds and it is 
# always possible to win the game.
#
# Input Format
#
# The first line contains an integer, n (the total number of clouds).  
# The second line contains n space-separated integers describing the respective
# values of clouds c(0),c(1),...,c(n-1). Each cloud is described as follows:
#
# - If c(i) = 0, then cloud i is an ordinary cloud.
# - If c(i) = 1, then cloud i is a thundercloud.
#
# Constraints
#
# 2 <= n <= 25
# c(i) = {0,1}
# c(0) = c(n-1) = 0
#
# Output Format 
#
# Print the minimum number of jumps needed to win the game.
#
# Example 0
#
# Given Input:
# 7
# 0 0 1 0 0 1 0
#
# Output:
# 4
#
# Explanation:
# Because c(2) and c(5) in our input are both 1, Emma must avoid c(2) and c(5). 
# Bearing this in mind, she can win the game with a minimum of 4 jumps:
# 0 -> 1, 1 -> 3, 3 -> 4, 4 -> 6
#
# Example 0
#
# Given Input:
# 6
# 0 0 0 0 1 0
#
# Output:
# 3
#
# Explanation:
# The only thundercloud to avoid is c(4). Emma can win the game in 3 jumps:
# 0 -> 2, 2 -> 3, 3 -> 5
#
# Solution
"""

n = int(input().strip())
c = [int(c_temp) for c_temp in input().strip().split(' ')]

cloud = 0
jumps = 0
while cloud < n - 1:
    print("cloud => ", cloud)
    if (cloud + 2 <= n -1) and (c[cloud + 2] == 0):  # Regular Cloud
        cloud += 2
    else:                                            # Thunder Cloud
        cloud += 1
    jumps += 1
        
print(jumps)