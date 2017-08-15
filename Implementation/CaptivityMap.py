#!/bin/python3
import sys
"""
# Description
# Difficulty: Easy
# 
# You are given a square map of size n X n. Each cell of the map has a value 
# denoting its depth. We will call a cell of the map a cavity if and only if 
# this cell is not on the border of the map and each cell adjacent to it has 
# strictly smaller depth. Two cells are adjacent if they have a common side (edge).
#
# You need to find all the cavities on the map and depict them with the uppercase
# character X.
#
# Input Format
#
# The first line contains an integer, n, denoting the size of the map. Each of 
# the following n lines contains n positive digits without spaces. Each digit 
# (1-9) denotes the depth of the appropriate area.
#
# Constraints
#
# 1 <= n <= 100
#
# Output Format 
#
# Output n lines, denoting the resulting map. Each cavity should be replaced 
# with character X.
#
# Example 0
#
# Given Input:
# 4
# 1112
# 1912
# 1892
# 1234
#
# Output:
# 1112
# 1X12
# 18X2
# 1234
#
# Explanation:
# The two cells with the depth of 9 fulfill all the conditions of the Cavity 
# definition and have been replaced by X.
#
# Solution
# 
"""
n = int(input().strip())
grid = []
grid_i = 0
for grid_i in range(n):
   grid_t = str(input().strip())
   grid.append(grid_t)

newGrid = [[-1 for x in range(n)] for y in range(n)] 

for row in range(n):
    for col in range(n):
        if row == 0 or row == n - 1 or col == 0 or col == n - 1:
            newGrid[row][col] = grid[row][col]
        elif (grid[row-1][col] < grid[row][col] and
              grid[row][col-1] < grid[row][col] and
              grid[row][col+1] < grid[row][col] and
              grid[row+1][col] < grid[row][col]):
            newGrid[row][col] = "X"
        else:
            newGrid[row][col] = grid[row][col]
            
for i in range(n):
    print(''.join(newGrid[i]))