#!/bin/python3

import sys
"""
# Taum is planning to celebrate the birthday of his friend, Diksha. There are 
# two types of gifts that Diksha wants from Taum: one is black and the other 
# is white. To make her happy, Taum has to buy B number of black gifts and W 
# number of white gifts.
#
# The cost of each black gift is X units.
# The cost of every white gift is Y units.
# The cost of converting each black gift into white gift or vice versa is Z units.
#
# Help Taum by deducing the minimum amount he needs to spend on Diksha's gifts.
# 
# Input Format
#
# The first line will contain an integer T which will be the number of test cases.
# There will be T pairs of lines. The first line of each test case will contain
# the values of integers B and W. Another line of each test case will contain 
# the values of integers X, Y, and Z.
#
# Constraints
#
# 1 <= T <= 10
# 0 <= X,Y,Z,B,W <= 10**9
#
# Output Format 
# T lines, each containing an integer: the minimum amount of units Taum needs 
# to spend on gifts.
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
# Needed help on this one...
"""

t = int(input().strip())
for a0 in range(t):
    b,w = input().strip().split(' ')
    b,w = [int(b),int(w)]
    x,y,z = input().strip().split(' ')
    x,y,z = [int(x),int(y),int(z)]

    print(min(x, y+z) * b + min(y, x+z) * w)
    
#    if (x < y) and ((z < x) or (z < y)):                     # Buy black and convert to white
#        print((b * x) + ((w * x) + (w * z)))
#    elif (x > y) and ((z < x) or (z < y)):                   # Buy white and convert to black
#        print((w * y) + ((b * y) + (b * z)))
#    else:                                       # Dont convert any gifts
#        print((b * x) + (w * y))
        