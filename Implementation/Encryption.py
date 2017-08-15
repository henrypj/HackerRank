#!/bin/python3

import sys
"""
# Description
# Difficulty: Medium
# 
# An English text needs to be encrypted using the following encryption scheme. 
# First, the spaces are removed from the text. Let  be the length of this text. 
# Then, characters are written into a grid, whose rows and columns have the 
# following constraints:
#
# floor(sqrt(L)) <= row <= column <= ceil(sqrt(L))
#
# For example, the sentence "if man was meant to stay on the ground god would
# have given us roots" after removing spaces is 54 characters long so it is 
# written in the form of a grid with 7 rows and 8 columns.
#
# ifmanwas
# meanttos
# tayonthe
# groundgo
# dwouldha
# vegivenu
# sroots
# 
# Ensure that rows x columns >= L
# If multiple grids satisfy the above conditions, the on with the minimum
# area (i.e. rows x columns)
#
# The encoded message is obtained by displaying the characters in a column, 
# inserting a space, and then displaying the next column and inserting a space,
# and so on. For example, the encoded message for the above rectangle is:
#
# imtgdvs fearwer mayoogo anouuio ntnnlvt wttddes aohghn sseoau
#
# You will be given a message in English with no spaces between the words. The 
# maximum message length can be 81 characters. Print the encoded message.     
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
# haveaniceday
#
# Output:
# hae and via ecy
#
# Explanation:
#
# Example
# 
# Given Input:
# feedthedog
#
# Output:
# fto ehg ee dd
#
# Solution
# 
"""
from math import sqrt, floor, ceil
s = input().strip()
s = s.replace(" ", "")
rows = floor(sqrt(len(s)))
cols = ceil(sqrt(len(s)))

# Ensure rows x cols >= len(s), if not
if rows * cols < len(s):
    rows += 1

grid = [[ "" for x in range(cols)] for y in range(rows)]
encodedMessage = ""

i = 0
for row in range(rows):
    for col in range(cols):
        grid[row][col] = s[i]
        i += 1
        if i >= len(s):
            break

for col in range(cols):
    for row in range(rows):
        encodedMessage += grid[row][col]
    encodedMessage += " "
print(encodedMessage)