#!/bin/python3

import sys
"""
# Aerith is playing a cloud game! In this game, there are n clouds numbered 
# sequentially from 0 to n - 1. Each cloud is either an ordinary cloud or a 
# thundercloud.
#
# Aerith starts out on cloud 0 with energy level E = 100. She can use 1 unit 
# of energy to make a jump of size k to cloud (i + k) % n, and she jumps until 
# she gets back to cloud 0. If Aerith lands on a thundercloud, her energy (E)
# decreases by 2 additional units. The game ends when Aerith lands back on cloud 0.
#
# Given the values of n, k, and the configuration of the clouds, can you 
# determine the final value of E after the game ends?
#
# Input Format
#
# The first line contains two space-separated integers, n (the number of clouds)
# and k (the jump distance), respectively. 
# The second line contains n space-separated integers describing the respective
# values of clouds c(0),c(1),...,c(n-1). Each cloud is described as follows:
#
# - If c(i) = 0, then cloud i is an ordinary cloud.
# - If c(i) = 1, then cloud i is a thundercloud.
#
# Constraints
#
# 2 <= n <= 25
# 1 <= k <= n
# n % k = 0
# c(i) = {0,1}
#
# Output Format 
#
# Print the final value of  on a new line.
#
# Example
#
# Given Input:
# 8 2
# 0 0 1 0 0 1 1 0
#
# Output:
# 92
#
# Explanation:
# 1. Move: 0 --> 2, Energy: E = 100 - 1 - 2 = 97
# 2. Move: 2 --> 4, Energy: E = 97 - 1 = 96
# 3. Move: 4 --> 6, Energy: E = 96 - 1 - 2 = 93
# 4. Move: 6 --> 0, Energy: E = 93 - 1 = 92
#
# Solution
"""

n,k = input().strip().split(' ')
n,k = [int(n),int(k)]
c = [int(c_temp) for c_temp in input().strip().split(' ')]

backOnZero = False
energy = 100
cloud  = 0
while not backOnZero:
    cloud = (cloud + k) % n
    energy -= 1
    if c[cloud] == 1:
        energy -= 2
    if cloud == 0:
        backOnZero = True
print(energy)