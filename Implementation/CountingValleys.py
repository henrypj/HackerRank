#!/bin/python3

import sys

# Gary is an avid hiker. He tracks his hikes meticulously, paying close 
# attention to small details like topography. During his last hike, he took 
# exactly n steps. For every step he took, he noted if it was an uphill or a 
# downhill step. Gary's hikes start and end at sea level. We define the 
# following terms:
#
# A mountain is a non-empty sequence of consecutive steps above sea level, 
# starting with a step up from sea level and ending with a step down to sea level.
#
# A valley is a non-empty sequence of consecutive steps below sea level, 
# starting with a step down from sea level and ending with a step up to sea level.
#
# Given Gary's sequence of up and down steps during his last hike, find and 
# print the number of valleys he walked through.
# 
# Input Format
# 
# The first line contains an integer, , denoting the number of steps in Gary's hike.
# The second line contains a single string of n characters. Each character is {U,D}
# (where U indicates a step up and D indicates a step down), and the i'th character 
# in the string describes Gary's i'th step during the hike.
# 
# Output Format
# 
# Print a single integer denoting the number of valleys Gary walked through 
# during his hike.


n = int(input().strip())
steps = input()

base       = 0
level      = 0
numValleys = 0
inValley   = False

for step in steps:
    if inValley:
        if step == "U":
            level += 1
            if level >= base:   # Out of valley
                inValley = False
        else:
            level -= 1
    else:
        if step == "U":
            level += 1
        else:
            level -= 1
            if level < base:   # In a valley
                inValley = True
                numValleys += 1
            
print(numValleys)

