#!/bin/python3

import sys
"""
# Description
# Difficulty: Medium
# 
# Given the time in numerals we may convert it into words, as shown below:
#
# 5:00 --> five o'clock
# 5:01 --> one minute past five
# 5:10 --> ten minutes past five
# 5:15 --> quarter past five
# 5:28 --> twenty eight minutes past five
# 5:30 --> half past five
# 5:40 --> twenty minutes to six
# 5:45 --> quarter to six
# 5:47 --> thirteen minutes to six
# 
# Write a program which prints the time in words for the input given in the
# format mentioned above.
# 
# Input Format
#
# There are two lines of input:
# H, representing the hours
# M, representing the minutes
#
# Constraints
#
# 1 <= H <= 12
# 0 <= M < 60
#
# Output Format 
#
# Display the time in words
#
# Example
#
# Given Input:
# 5
# 47
#
# Output:
#
# thirteen minutes to six
#
# Explanation:
#
#
# Solution
# 
"""
h = int(input().strip())
m = int(input().strip())

numToWord = {}
numToWord[0]  = "o'clock"
numToWord[1]  = "one"
numToWord[2]  = "two"
numToWord[3]  = "three"
numToWord[4]  = "four"
numToWord[5]  = "five"
numToWord[6]  = "six"
numToWord[7]  = "seven"
numToWord[8]  = "eight"
numToWord[9]  = "nine"
numToWord[10] = "ten"
numToWord[11] = "eleven"
numToWord[12] = "twelve"
numToWord[13] = "thirteen"
numToWord[14] = "fourteen"
numToWord[15] = "quarter"
numToWord[16] = "sixteen"
numToWord[17] = "seventeen"
numToWord[18] = "eighteen"
numToWord[19] = "nineteen"
numToWord[20] = "twenty"
numToWord[21] = "twenty one"
numToWord[22] = "twenty two"
numToWord[23] = "twenty three"
numToWord[24] = "twenty four"
numToWord[25] = "twenty five"
numToWord[26] = "twenty six"
numToWord[27] = "twenty seven"
numToWord[28] = "twenty eight"
numToWord[29] = "twenty nine"
numToWord[30] = "half"
numToWord[31] = "twenty nine"
numToWord[32] = "twenty eight"
numToWord[33] = "twenty seven"
numToWord[34] = "twenty six"
numToWord[35] = "twenty five"
numToWord[36] = "twenty four"
numToWord[37] = "twenty three"
numToWord[38] = "twenty two"
numToWord[39] = "twenty one"
numToWord[40] = "twenty"
numToWord[41] = "nineteen"
numToWord[42] = "eighteen"
numToWord[43] = "seventeen"
numToWord[44] = "sixteen"
numToWord[45] = "quarter"
numToWord[46] = "fourteen"
numToWord[47] = "thirteen"
numToWord[48] = "twelve"
numToWord[49] = "eleven"
numToWord[50] = "ten"
numToWord[51] = "nine"
numToWord[52] = "eight"
numToWord[53] = "seven"
numToWord[54] = "six"
numToWord[55] = "five"
numToWord[56] = "four"
numToWord[57] = "three"
numToWord[58] = "two"
numToWord[59] = "one"

if m == 0:
    print(numToWord[h] + " " + numToWord[0])
elif m == 15 or m == 30:
    print(numToWord[m] + " past " + numToWord[h])    
elif m == 45:
    print(numToWord[m] + " to " + numToWord[h + 1])
elif m < 30:
    print(numToWord[m] + " minutes past " + numToWord[h])
else:
    print(numToWord[m] + " minutes to " + numToWord[h + 1])
