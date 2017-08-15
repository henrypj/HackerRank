#!/bin/python3

import sys
"""
#
# Input Format
#
#
# Constraints
#
#
# Output Format 
#
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
 