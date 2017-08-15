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
"""
##############
# SOLUTION 2 #
##############
from copy import deepcopy
R,C,N = input().strip().split(' ')
R,C,N = [int(R),int(C),int(N)]
G  = []

Gsec = [[0 for x in range(C)] for y in range(R)]
all_bombs = [['O' for x in range(C)] for y in range(R)]
FILENAME = 'bomberman.txt'

# Used the following to test with one of the test cases 200 187 5
#
#def load_rows(rows):
#    """
#    Returns a list of rows that make up the test cas
#    """
#    rowlist = []
#    print("Loading rows from file...")
#    # inFile: file
#    inFile = open(FILENAME, 'r')
#    # line: string
#    for r in range(rows):
#        line = inFile.readline()
#        rowlist.append(list(line.strip()))
#    print("  ", len(rowlist), "rowss loaded.")
#    return rowlist
#
#G = load_rows(R)


for c in range(R):
    G.append(list(input().strip()))

for sec in range(7):    # Only need to generate up to 7 patterns
    print("Second => ", sec)
    if sec % 2 == 0 and sec != 0:   # Plant bombs
        for row in range(R):
            for col in range(C):
                if G[row][col] == ".":
                    G[row][col]    = "O"
                    Gsec[row][col] = 1
                else:
                    Gsec[row][col] += 1
    else:
        for row in range(R):
            for col in range(C):
                if G[row][col] == "O" and Gsec[row][col] == 3:   # Bonb detonates
                    G[row][col]    = "."
                    Gsec[row][col] = 0
                    # Detonate neighboring cells
                    if row >= 1:
                        G[row - 1][col]    = "."
                        Gsec[row - 1][col] = 0
                    if row < R - 1 and Gsec[row + 1][col] != 3:    
                        G[row + 1][col]    = "."
                        Gsec[row + 1][col] = 0
                    if col >= 1:
                        G[row][col - 1]    = "."
                        Gsec[row][col - 1] = 0
                    if col < C - 1 and Gsec[row][col + 1] != 3:
                        G[row][col + 1]    = "."
                        Gsec[row][col + 1] = 0
                elif G[row][col] == "O" and Gsec[row][col] < 3:
                    Gsec[row][col] += 1
#
#    for row in G:    
#        print(''.join(str(x) for x in row))
#    print("\r")
#
    if sec == 1:
        G1 = deepcopy(G)
    elif sec == 3:
        G3 = deepcopy(G)
    elif sec == 5:
        G5 = deepcopy(G)

if N == 0 or N == 1:
    for row in G1:
        print(''.join(str(x) for x in row))
elif N % 2 == 0:
    for row in all_bombs:    
        print(''.join(str(x) for x in row))
elif N % 4 == 1:        
    for row in G5:    
        print(''.join(str(x) for x in row))
elif N % 4 == 3:
    for row in G3:    
        print(''.join(str(x) for x in row))



##############
# SOLUTION 1 #
##############
#R,C,N = input().strip().split(' ')
#R,C,N = [int(R),int(C),int(N)]
#G = []
#Gsec = [[0 for x in range(C)] for y in range(R)]
#
#for c in range(R):
#    G.append(list(input().strip()))
#
#for sec in range(N + 1):
#    print("SECOND => ", sec)
#    if sec % 2 == 0 and sec != 0:   # Plant bombs
#        for row in range(R):
#            for col in range(C):
#                if G[row][col] == ".":
#                    G[row][col]    = "O"
#                    Gsec[row][col] = 1
#                else:
#                    Gsec[row][col] += 1
#    else:
#        for row in range(R):
#            for col in range(C):
#                if G[row][col] == "O" and Gsec[row][col] == 3:   # Bonb detonates
#                    G[row][col]    = "."
#                    Gsec[row][col] = 0
#                    # Detonate neighboring cells
#                    if row >= 1:
#                        G[row - 1][col]    = "."
#                        Gsec[row - 1][col] = 0
#                    if row < R - 1 and Gsec[row + 1][col] != 3:    
#                        G[row + 1][col]    = "."
#                        Gsec[row + 1][col] = 0
#                    if col >= 1:
#                        G[row][col - 1]    = "."
#                        Gsec[row][col - 1] = 0
#                    if col < C - 1 and Gsec[row][col + 1] != 3:
#                        G[row][col + 1]    = "."
#                        Gsec[row][col + 1] = 0
#                elif G[row][col] == "O" and Gsec[row][col] < 3:
#                    Gsec[row][col] += 1
#    
#    for row in G:    
#        print(''.join(str(x) for x in row))
#    print("\r")
#    for row in Gsec:
#        print(''.join(str(x) for x in row))
#    print("\r")
