#!/bin/python3
import sys
"""
# Description
# Difficulty: Easy
# 
# Happy Ladybugs is a board game having the following properties:
# - The board is represented by a string, b, of length b. The i'th character 
#   of the string, b(i), denotes the i'th cell of the board. 
#   * If b(i) is an underscore (i.e., _), it means the i'th cell of the board
#     is empty.
#   * If b(i) is an uppercase English alphabetic letter (i.e., A through Z), 
#     it means the i'th cell contains a ladybug of color b(i) 
#   * String b will not contain any other characters.
#
# - A ladybug is happy only when its left or right adjacent cell (i.e. b(i-1), 
#   b(i+1) is occupied by another ladybug having the same color.
#
# - In a single move, you can move a ladybug from its current position to any 
#   empty cell. 
#
# Given the values of n and b for g games of Happy Ladybugs, determine if it's 
# possible to make all the ladybugs happy. For each game, print YES on a new 
# line if all the ladybugs can be made happy through some number of moves; 
# otherwise, print NO to indicate that no number of moves will result in all 
# the ladybugs being happy..
#
# Input Format
#
# The first line contains an integer, g, denoting the number of games. The 
# 2 * g subsequent lines describes a Happy Ladybugs game in the following format:
# 
# 1. The first line contains an integer, n, denoting the number of cells on the
#    board.
#
# 2. The second line contains a string, b, describing the n cells of the board.
#
# Constraints
#
# 1 <= g <= 100
# 1 <= n <= 100
# It is guaranteed that string b consists of underscores and/or uppercase 
# English alphabetic letters (i.e., _ and A through Z).
#
# Output Format 
#
# For each game, print YES on a new line if it is possible to make all the 
# ladybugs happy; otherwise, print NO.
#
# Example 0
#
# Given Input:
# 4
# 7
# RBY_YBR
# 6
# X_Y__X
# 2
# __
# 6
# B_RRBR
#
# Output:
# YES
# NO
# YES
# YES
#
# Explanation:
# The first three games of Happy Ladybugs is described below:
#
# 1. Initial Board:
#      0   1   2   3   4   5   6    
#    +---+---+---+---+---+---+---+
#    | R | B | Y | _ | Y | B | R |
#    +---+---+---+---+---+---+---+
#
#    After the first move:
#      0   1   2   3   4   5   6    
#    +---+---+---+---+---+---+---+
#    | R | B | Y | Y | _ | B | R |
#    +---+---+---+---+---+---+---+
#
#    After the second move:
#      0   1   2   3   4   5   6    
#    +---+---+---+---+---+---+---+
#    | R | _ | Y | Y | B | B | R |
#    +---+---+---+---+---+---+---+
#
#    After the third move:
#      0   1   2   3   4   5   6    
#    +---+---+---+---+---+---+---+
#    | R | R | Y | Y | B | B | _ |
#    +---+---+---+---+---+---+---+
#
#    Now all the ladybugs are happy, so we print YES on a new line.
#
# 2. There is no way to make the ladybug having color Y happy, so we print NO 
#    on a new line.
#
# 3. There are no unhappy ladybugs, so we print YES on a new line.
#
# Solution
"""
Q = int(input().strip())
for a0 in range(Q):
    n = int(input().strip())
    b = input().strip()

    happy = True
    bDict = {}
    numBlanks = b.count('_')    
    bNew = b.replace("_","")
    bNewLen = len(bNew)
       
    for i in range(bNewLen):
        bDict[bNew[i]] = bDict.get(bNew[i],0) + 1
        if bNewLen == 1 and numBlanks != 1:
            happy = False
        else:
            if i == 0 and n > 1:
                if bNew[i] != bNew[i+1]:
                    happy = False
            elif i == bNewLen - 1 and bNewLen > 1:
                if bNew[i] != bNew[i-1]:
                    happy = False
            else:
                if bNew[i] != bNew[i-1] and bNew[i] != bNew[i+1]:
                    happy = False
    
    if not happy and numBlanks > 0:
        happy = True
        for ladybug, numLadybugs in bDict.items():
            if numLadybugs == 1:
                happy = False
                break
    if happy:
        print("YES")
    else:
        print("NO")    