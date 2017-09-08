#!/bin/python3
import sys
"""
# Description
# Difficulty: Medium
# 
# Ema built a quantum computer! Help her test its capabilities by solving the 
# problem below.
#
# Given a grid of size N x M, each cell in the grid is either good or bad.
#
# A valid plus is defined here as the crossing of two segments (horizontal and
# vertical) of equal lengths. These lengths must be odd, and the middle cell 
# of its horizontal segment must cross the middle cell of its vertical segment.
#
# In the diagram below, the top row of pluses are valid and the bottom row are
# not valid.
#
#                                          +---+
#                                          |   |
#                    +---+                 +---+
#                    |   |                 |   |
#      +---+     +---+---+---+     +---+---+---+---+---+
#      |   |     |   |   |   |     |   |   |   |   |   |
#      +---+     +---+---+---+     +---+---+---+---+---+
#                    |   |                 |   |
#                    +---+                 +---+
#                                          |   |
#                                          +---+
#
#          +---+                 +---+             +---+
#          |   |                 |   |             |   |
#      +---+---+---+---+     +---+---+---+---+     +---+---+---+
#      |   |   |   |   |     |   |   |   |   |     |   |   |   |
#      +---+---+---+---+     +---+---+---+---+     +---+---+---+
#          |   |                 |   |             |   |
#          +---+                 +---+             +---+
#          |   |
#          +---+
#
# Find the 2 valid pluses that can be drawn on good cells in the grid, and print
# an integer denoting the maximum product of their areas.
#
# Note: The two pluses cannot overlap, and the product of their areas should be 
# maximal.
#
# Input Format
#
# The first line contains two space-separated integers, N and M.
# The N subsequent lines contains M characters, where each character is either
# G (good) or B (bad). If the y'th character in the x'th line is G, then (x,y) 
# is a good cell (otherwise it's a bad cell).
#
# Constraints
#
# 2 <= N <= 15
# 2 <= M <= 15
#
# Output Format 
#
# Find  pluses that can be drawn on good cells of the grid, and print an integer
# denoting the maximum product of their areas.
#
# Example 0
#
# Given Input:
# 5 6
# GGGGGG
# GBBBGB
# GGGGGG
# GGBBGB
# GGGGGG
#
# Output:
# 5
#
# Example 1
#
# Given Input:
# 6 6
# BGBBGB
# GGGGGG
# BGBBGB
# GGGGGG
# BGBBGB
# BGBBGB
#
# Output:
# 25
#
# Explanation:
# Here are the two possible solutions for Example 0 (left) and Example 1 (right):
#
#      +---+---+---+---+---+---+          +---+===+---+---+---+---+
#      | G | G | G | G | G | G |          | R | B | R | R | G | R |
#      +---+---+---+---+===+---+          +===+===+===+---+---+---+
#      | G | R | R | R | B | R |          | B | B | B | G | G | G |
#      +---+---+---+===+===+===+          +===+===+===+---+===+---+
#      | G | B | G | B | B | B |          | R | B | R | R | B | R |
#      +---+---+---+===+===+===+          +---+===+---+===+===+===+
#      | G | G | R | R | B | R |          | G | G | G | B | B | B |
#      +---+---+---+---+===+---+          +---+---+---+===+===+===+
#      | G | G | G | G | G | G |          | R | G | R | R | B | R |
#      +---+---+---+---+---+---+          +---+---+---+---+===+---+
#                                         | R | G | R | R | G | R |
#                                         +---+---+---+---+---+---+
#
# G = green, good cell
# R = red, bad cell
# B = blue, possible pluses
#
# For the explanation below, we will refer to a plus of length i as P(i).
#
# Sample 0:
# There is enough good space to color one P(3) plus and one P(1) plus. Area(P(3))
# = 5 units, and Area(P(1)) = 1 unit. The product of their areas is 5, so we print 5.
#
# Sample 1:
# There is enough good space to color two P(3) pluses. Area(P(3)) = 5 units. The 
# product of the areas of our two P(3) pluses is 5 x 5 = 25, so we print 25.
#
# Solution:
# 
# NOTE THE SOLUTIONS BELOW ARE SAMPLE CODE ONLY, NOT SOLUTIONS TO THIS
#
"""
##############
# SOLUTION 1 #
##############
G  = []
N,M = input().strip().split(' ')
N,M = [int(N),int(M)]
for i in range(N):
    G.append((input().strip()).split())
#    G.append(list(input().strip()))
print(G)

print(G[0])
print(G[0][1])
print(G[1])
#for row in range(N):
#    print("row => ", row)
#    for col in range(M):
#        print("col => ", col)
#        print(G[row][col])












































