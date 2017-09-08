#!/bin/python3
import sys
"""
# Description
# Difficulty: Easy
# 
# Sami's spaceship crashed on Mars! She sends  sequential SOS messages to Earth
# for help.
#
# Letters in some of the SOS messages are altered by cosmic radiation during 
# transmission. Given the signal received by Earth as a string, S, determine how
# many letters of Sami's SOS have been changed by radiation.
#
# Input Format
#
# There is one line of input: a single string, S.
#
# Note: As the original message is just SOS repeated n times, S's length will be
# a multiple of 3.
#
# Constraints
#
# 1 <= |S| <= 99
# |S| % 3 = 0
# S will only contain uppercase English letters.
#
# Output Format 
#
# Print the number of letters in Sami's message that were altered by cosmic radiation.
#
# Example 0
#
# Given Input:
# SOSSPSSQSSOR
#
# Output:
# 3
#
# Example 1
#
# Given Input:
# SOSSOT
#
# Output:
# 1
#
# Explanation:
# Test Case 0
# S = SOSSPSSQSSOR, and signal length |S| = 12. Sami sent 4 SOS messages 
# (i.e.: 12/3 = 4).
#
# Expected signal: SOSSOSSOSSOS
# Recieved signal: SOSSPSSQSSOR
#
# We print the number of changed letters, which is 3.
#
# Test Case 1
# S = SOSSOT, and signal length |S| = 6. Sami sent 2 SOS messages (i.e.: 6/3 = 2).
#
# Expected Signal: SOSSOS 
# Received Signal: SOSSOT
#
# We print the number of changed letters, which is 1.
#
# Solution:
#    
"""
S = input().strip()
lenS = len(S)
numMsgs = lenS // 3
msgNum = 0
changedLetters = 0

for i in range(lenS):
    if i % 3 == 0:
        msgNum += 1
    if msgNum % 2 == 0:          # Even message
        if i % 2 == 0:           # Even index
            if S[i] != "O":
                changedLetters += 1
        else:                   # Odd index
            if S[i] != "S":
                changedLetters += 1
    else:                       # Odd message
        if i % 2 == 0:          # Even index
            if S[i] != "S":
                changedLetters += 1
        else:                   # Odd index
            if S[i] != "O":
                changedLetters += 1
                
print(changedLetters)