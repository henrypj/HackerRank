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
# the four diagonals). In the diagram below, the "O" denote all the cells the
# queen can attack from :
#
#          +---+---+---+---+---+---+---+---+
#        8 |   |   |   | O |   |   |   | O |
#          +---+---+---+---+---+---+---+---+
#        7 | X |   |   | O |   |   | O |   |
#          +---+---+---+---+---+---+---+---+
#        6 |   | X |   | O |   | X |   |   |
#          +---+---+---+---+---+---+---+---+
#        5 |   |   | X | O | X |   |   |   |
#          +---+---+---+---+---+---+---+---+
#        4 | X | X | X | # | X | X | X | X |
#          +---+---+---+---+---+---+---+---+
#        3 |   |   | X | O | X |   |   |   |
#          +---+---+---+---+---+---+---+---+
#        2 |   | X |   | O |   | X |   |   |
#          +---+---+---+---+---+---+---+---+
#        1 | X |   |   | O |   |   | X |   |
#          +---+---+---+---+---+---+---+---+
#            1   2   3   4   5   6   7   8
#
# There are K obstacles on the chessboard preventing the queen from attacking 
# any square that has an obstacle blocking the the queen's path to it. For 
# example, an obstacle at location (3,5) in the diagram above would prevent the
# queen from attacking cells (3,5), (2,6), and (1,7):
#
#          +---+---+---+---+---+---+---+---+
#        8 |   |   |   | X |   |   |   | X |
#          +---+---+---+---+---+---+---+---+
#        7 | X |   |   | X |   |   | X |   |
#          +---+---+---+---+---+---+---+---+
#        6 |   | X |   | X |   | X |   |   |
#          +---+---+---+---+---+---+---+---+
#        5 |   |   | X | X | X |   |   |   |
#          +---+---+---+---+---+---+---+---+
#        4 | X | X | X | Q | X | X | X | X |
#          +---+---+---+---+---+---+---+---+
#        3 |   |   | X | X | * |   |   |   |
#          +---+---+---+---+---+---+---+---+
#        2 |   | X |   | X |   | * |   |   |
#          +---+---+---+---+---+---+---+---+
#        1 | X |   |   | X |   |   | * |   |
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
# Example
#
# Given Input:
# 4 0
# 4 4
#
# Output:
# 9
#
# Explanation:
#
# The queen is standing at position (4,3) on a 5 x 5 chessboard with no obstacles:
#
#          +---+---+---+---+---+
#        5 |   |   |   |   |   |
#          +---+---+---+---+---+
#        4 |   |   | Q |   |   |
#          +---+---+---+---+---+
#        3 |   |   |   |   |   |
#          +---+---+---+---+---+
#        2 |   |   |   |   |   |
#          +---+---+---+---+---+
#        1 |   |   |   |   |   |
#          +---+---+---+---+---+
#            1   2   3   4   5  
#
# Solution
# Save for later...
"""

#n,k = input().strip().split(' ')
#n,k = [int(n),int(k)]
#rQueen,cQueen = input().strip().split(' ')
#rQueen,cQueen = [int(rQueen),int(cQueen)]
#for a0 in range(k):
#    rObstacle,cObstacle = input().strip().split(' ')
#    rObstacle,cObstacle = [int(rObstacle),int(cObstacle)]
    # your code goes here
n = 5
k = 3
rQueen = 4
cQueen = 3 
rObstacle = 4
cObstacle = 2
board = [[0 for x in range(n)] for y in range(n)]

# Calculate distance of Queen to board edges
Qn  = n - rQueen
Qne = n - max(rQueen, cQueen)
Qe  = n - cQueen
Qse = min(n-cQueen, rQueen-1)
Qs  = rQueen - 1
Qsw = min(rQueen, cQueen) - 1
Qw  = cQueen - 1
Qnw = min(n-rQueen, abs(1-cQueen))


print(Qn, Qne, Qe, Qse, Qs, Qsw, Qw, Qnw)

if rObstacle == rQueen:
    if cObstacle < cQueen and cQueen - cObstacle < Qw:
        Qw = cQueen - cObstacle
    elif cObstacle > cQueen and cObstacle - cQueen < Qe:
        Qe = cObstacle - cQueen
elif rObstacle > rQueen:
    if cObstacle < cQueen and 

for row in range(n):
    for col in range(n):
        if row == rQueen:
            board[row][col] = 1
        if col == cQueen:
            board[row][col] = 1

print(board)
 