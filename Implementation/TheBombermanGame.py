#!/bin/python3
import sys
"""
# Description
# Difficulty: Medium
# 
# Bomberman lives in a rectangular grid with R rows and C columns. Each cell in
# the grid either contains a bomb or nothing at all.
#
# Each bomb can be planted in any cell of the grid but, once planted, it will 
# detonate after exactly 3 seconds. Once a bomb detonates, it's destroyed — 
# along with anything in its four neighboring cells. This means that if a bomb 
# detonates in cell i, j cells (i += 1,j) and (i,j += 1) are cleared (note that
# cells at the edge of the grid have less than four neighboring cells). If there
# is a bomb in a neighboring cell, the neighboring bomb is destroyed without 
# detonating (i.e., no chain reaction occurs).
#
# Bomberman is immune to bombs, so he can move freely throughout the grid. Here's
# what he does:
#
# 1. Initially, Bomberman arbitrarily plants bombs in some of the cells.
# 2. After one second, Bomberman does nothing.
# 3. After one more second, Bomberman plants bombs in all cells without bombs,
#    thus filling the whole grid with bombs. It is guaranteed that no bombs will
#    detonate at this second.
# 4. After one more second, any bombs planted exactly three seconds ago will 
#    detonate. Here, Bomberman stands back and observes.
# 5. Bomberman then repeats steps 3 and 4 indefinitely.
#
# Note that during every second Bomberman plants bombs, the bombs are planted
# simultaneously (i.e., at the exact same moment), and any bombs planted at the
# same time will detonate at the same time.
#
# Given the initial configuration of the grid with the locations of Bomberman's
# first batch of planted bombs, determine the state of the grid after N seconds.
#
# Input Format
#
# The first line contains three space-separated integers denoting the respective
# values of R, C, and N. 
# Each line i of the R subsequent lines describes row i of the grid's initial 
# state as a single string of C characters; the "." character denotes an empty
# cell, and the O character (ascii 79) denotes a bomb.
#
# Constraints
#
# 1 <= R,C <= 200
# 1 <= N <= 10**9
# 1 <= N <= 200 for 40% of the maximum score.
#
# Output Format 
#
# Print the grid's final state. This means R lines where each line contains C 
# characters, and each character is either a . or an O (ascii 79). This grid 
# must represent the state of the grid after N seconds.
#
# Example 0
#
# Given Input:
# 6 7 3
# .......
# ...0...
# ....0..
# .......
# 00.....
# 00.....
#
# Output:
# 000.000
# 00...00
# 000...0
# ..00.00
# ...0000
# ...0000
#
# Explanation:
# The initial state of the grid is as follows:
# .......
# ...0...
# ....0..
# .......
# 00.....
# 00.....
#    
# Bomberman spends the first second doing nothing, so the state after 1 second is: 
# .......
# ...0...
# ....0..
# .......
# 00.....
# 00.....
#
# Bomberman then plants bombs in all the empty cells during his second second,
# so this is the result after 2 seconds: 
# 0000000
# 0000000
# 0000000
# 0000000
# 0000000
# 0000000
#
# In his third second, Bomberman sits back and watches all the bombs he planted
# 3 seconds ago detonate. This is the final state after 3 seconds:
# 000.000
# 00...00
# 000...0
# ..00.00
# ...0000
# ...0000
#
# Example 1:
# 
# Given Input:
# 5 5 7
# ..OO.
# OO.O.
# ..O..
# .....
# O.O.O
#
# Output:
# .....
# .....
# ....O
# .O.O.
# .....
#
#
# Solution:
# My solution 1 functionally works, but times out on the larger N. After
# reading the discussion groups and testing with different input, I realized
# that there is no need to calculate the pattern for large N as there is a 
# repeating pattern. There are essentially 4 possibilities, the original input
# pattern, a pattern of all bombs, and two other patterns that repeat at 
# N % 4 == 3 (3,7,11,15...) and N % 4 == 1 (5,9,13,17...). Solution 2 calculates
# and saves these four patterns then displays the correct one for the given N.
# 
Seconds:    1       2      3     4     5      6      7     8     9
   0        1       2      3     2     3      2      3     2     3
initial, nothing, plant, boom, plant, boom, plant, boom, plant, boom 
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
