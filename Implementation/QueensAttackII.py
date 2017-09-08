#!/bin/python3

import sys
"""
# Description
# Difficulty: Medium
#
# A queen is standing on an n x n chessboard. The chessboard's rows are numbered
# from 1 to n, going from bottom to top; its columns are numbered from 1 to n, 
# going from left to right. Each square on the board is denoted by a tuple, (r, c), 
# describing the row, r, and column, c, where the square is located.
#
# The queen is standing at position (r(q), c(q)) and, in a single move, she can
# attack any square in any of the eight directions (left, right, up, down, or 
# the four diagonals). In the diagram below, the "√" denote all the cells the
# queen can attack from :
#
#          +---+---+---+---+---+---+---+---+
#        8 |   |   |   | √ |   |   |   | √ |
#          +---+---+---+---+---+---+---+---+
#        7 | √ |   |   | √ |   |   | √ |   |
#          +---+---+---+---+---+---+---+---+
#        6 |   | √ |   | √ |   | √ |   |   |
#          +---+---+---+---+---+---+---+---+
#        5 |   |   | √ | √ | √ |   |   |   |
#          +---+---+---+---+---+---+---+---+
#        4 | √ | √ | √ | Q | √ | X | √ | √ |
#          +---+---+---+---+---+---+---+---+
#        3 |   |   | √ | √ | √ |   |   |   |
#          +---+---+---+---+---+---+---+---+
#        2 |   | √ |   | √ |   | √ |   |   |
#          +---+---+---+---+---+---+---+---+
#        1 | √ |   |   | √ |   |   | √ |   |
#          +---+---+---+---+---+---+---+---+
#            1   2   3   4   5   6   7   8
#
# There are K obstacles on the chessboard preventing the queen from attacking 
# any square that has an obstacle blocking the the queen's path to it. For 
# example, an obstacle at location (3,5) in the diagram above would prevent the
# queen from attacking cells (3,5), (2,6), and (1,7):
#
#          +---+---+---+---+---+---+---+---+
#        8 |   |   |   | √ |   |   |   | √ |
#          +---+---+---+---+---+---+---+---+
#        7 | √ |   |   | √ |   |   | √ |   |
#          +---+---+---+---+---+---+---+---+
#        6 |   | √ |   | √ |   | √ |   |   |
#          +---+---+---+---+---+---+---+---+
#        5 |   |   | √ | √ | √ |   |   |   |
#          +---+---+---+---+---+---+---+---+
#        4 | √ | √ | √ | Q | √ | X | √ | √ |
#          +---+---+---+---+---+---+---+---+
#        3 |   |   | √ | √ | X |   |   |   |
#          +---+---+---+---+---+---+---+---+
#        2 |   | √ |   | √ |   |   |   |   |
#          +---+---+---+---+---+---+---+---+
#        1 | √ |   |   | √ |   |   |   |   |
#          +---+---+---+---+---+---+---+---+
#            1   2   3   4   5   6   7   8
#
# Given the queen's position and the locations of all the obstacles, find and 
# print the number of squares the queen can attack from her position at (r(q),c(q)).
#
# Input Format
#
# The first line contains two space-separated integers describing the respective
# values of n (the side length of the board) and k (the number of obstacles). 
#
# The next line contains two space-separated integers describing the respective
# values of r(q) and c(q), denoting the position of the queen. 
#
# Each line i of the k subsequent lines contains two space-separated integers 
# describing the respective values of and r(i), c(i) denoting the position of 
# obstacle i.
#
# Constraints
#
# 0 <= n <= 10**5
# 0 <= k <= 10**5
# A single cell may contain more than one obstacle; however, it is guaranteed 
# that there will never be an obstacle at position (r(q), c(q)) where the queen
# is located.
#
# Subtasks
#
# For 30% of the maximum score
# 0 <= n <= 100
# 0 <= k <= 100
#
# For 50% of the maximum score
# 0 <= n <= 1000
# 0 <= k <= 10**5
#
# Output Format 
#
# Print the number of squares that the queen can attack from position (r(q),c(q)).
#
# Example 0
#
# Given Input:
# 4 0
# 4 4
#
# Output:
# 9
#
# Explanation 0:
#
# The queen is standing at position (4,4) on a 4 x 4 chessboard with no obstacles:
#
#          +---+---+---+---+
#        4 | √ | √ | √ | Q |
#          +---+---+---+---+
#        3 |   |   | √ | √ |
#          +---+---+---+---+
#        2 |   | √ |   | √ |
#          +---+---+---+---+
#        1 | √ |   |   | √ |
#          +---+---+---+---+
#            1   2   3   4   
#
# We then print the number of squares she can attack from that position, which is 9.
#
# Example 1
#
# Given Input:
# 5 3
# 4 3
# 5 5
# 4 2
# 2 3
#
# Output:
# 10
#
# Explanation 1:
#
# The queen is standing at position (4,3) on a 5 x 5 chessboard with k=3 obstacles:
#
#          +---+---+---+---+---+
#        5 |   | √ | √ | √ | X |
#          +---+---+---+---+---+
#        4 |   | X | Q | √ | √ |
#          +---+---+---+---+---+
#        3 |   | √ | √ | √ |   |
#          +---+---+---+---+---+
#        2 | √ |   | X |   | √ |
#          +---+---+---+---+---+
#        1 |   |   |   |   |   |
#          +---+---+---+---+---+
#            1   2   3   4   5 
#
# Qn Qne Qe Qse Qs Qsw Qw Qnw
#  1  1   2  2   1  2   0  1
# We then print the number of squares she can attack from that position, which is 10.
#
# Solution
# Save for later...
"""

n,k = input().strip().split(' ')
n,k = [int(n),int(k)]
rQueen,cQueen = input().strip().split(' ')
rQueen,cQueen = [int(rQueen),int(cQueen)]

# Calculate distance of Queen to board edges
Qn  = n - rQueen
Qne = n - max(rQueen, cQueen)
Qe  = n - cQueen
Qse = min(n-cQueen, rQueen-1)
Qs  = rQueen - 1
Qsw = min(rQueen, cQueen) - 1
Qw  = cQueen - 1
Qnw = min(n-rQueen, abs(1-cQueen))

for a0 in range(k):
    rObstacle,cObstacle = input().strip().split(' ')
    rObstacle,cObstacle = [int(rObstacle),int(cObstacle)]

# Recalculate distances in each direction based on obstacles
    if rObstacle == rQueen and cObstacle < cQueen:            # Qw
        val = cQueen - 1 - cObstacle
        if val < Qw:
            Qw = val
            
    elif rObstacle == rQueen and cObstacle > cQueen:          # Qe
        val = cObstacle - cQueen - 1
        if val < Qe:
            Qe = val
    
    elif cObstacle == cQueen and rObstacle > rQueen:          # Qn
        val = rObstacle - rQueen - 1
        if val < Qn:
            Qn = val
    
    elif cObstacle == cQueen and rObstacle < rQueen:          # Qs
        val = rQueen - 1 - rObstacle
        if val < Qs:
            Qs = val
    
    elif abs(rQueen - rObstacle) == abs(cQueen - cObstacle):
        val = abs(rQueen - rObstacle) - 1
        if rQueen - rObstacle < 0 and cQueen - cObstacle < 0: # Qne
            if val < Qne:
                Qne = val
    
        elif rQueen - rObstacle < 0 and cQueen - cObstacle > 0: # Qnw
            if val < Qnw:
                Qnw = val
    
        elif rQueen - rObstacle > 0 and cQueen - cObstacle < 0: # Qse
            if val < Qse:
                Qse = val
    
        elif rQueen - rObstacle > 0 and cQueen - cObstacle > 0: # Qsw
            if val < Qsw:
                Qsw = val

total = Qn + Qne + Qe + Qse + Qs + Qsw + Qw + Qnw
print(total)

