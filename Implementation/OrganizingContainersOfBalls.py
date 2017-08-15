#!/bin/python3

import sys
"""
# Description
# Difficulty: Medium
# 
# Input Format
#
# Constraints
#
# Output Format 
#
# Example
#
# Given Input:
#
# Output:
#
# Explanation:
#
# Solution
# Needed guidance
# Key is that the containers may contain different number of balls, but they
# will contain the same number of balls after all swaps because we are
# swapping 1:1. Thus, in the end, the number of balls/container must equal
# the number of different types of balls.
"""

q = int(input().strip())
for a0 in range(q):
    n = int(input().strip())
    M = []
    for M_i in range(n):
        M_t = [int(M_temp) for M_temp in input().strip().split(' ')]
        M.append(M_t)
        # your code goes here

    numBallsPerContainer = [0] * n
    numBallsPerType      = [0] * n
    
    for container in range(n):
        for ball in range(n):
            numBallsPerContainer[container] += M[container][ball]
            numBallsPerType[ball]           += M[container][ball]

    numBallsPerContainer.sort()
    numBallsPerType.sort()
    
    possible = "Possible"
    for i in range(n):
        if numBallsPerContainer[i] != numBallsPerType[i]:
            possible = "Impossible"

    print(possible)
    
