#!/bin/python3

import sys
"""
# Description
# Difficulty: Easy
# 
# Here's an explanation from Wikipedia about the ORIGINAL Kaprekar Number 
# (spot the difference!): In mathematics, a Kaprekar number for a given base
# is a non-negative integer, the representation of whose square in that base 
# can be split into two parts that add up to the original number again. For 
# instance, 45 is a Kaprekar number, because 45² = 2025 and 20+25 = 45.
#
# You are given the two positive integers p and q, where p is lower than q. 
# Write a program to determine how many Kaprekar numbers are there in the range
# between p and q (both inclusive) and display them all.
#
# Input Format
#
# There will be two lines of input: p, lowest value q, highest value
#
# Constraints
#
# 0 < p < q < 100000
#
# Output Format 
#
# Output each Kaprekar number in the given range, space-separated on a single 
# line. If no Kaprekar numbers exist in the given range, print INVALID RANGE.
#
# Example
#
# Given Input:
# 1
# 100
#
# Output:
# 1 9 45 55 99
#
# Explanation:
#
# Solution
# 
"""
from math import ceil
    
p = int(input().strip())
q = int(input().strip())
kaprekarNumbers = ""

for num in range(p, q + 1):
    numSq = num ** 2
    numSqStr = str(numSq)
    numDigitsRight = ceil(len(numSqStr) / 2)
    numDigitsLeft  = len(numSqStr) - numDigitsRight
    digitsRight = numSqStr[-numDigitsRight:]
    digitsLeft  = numSqStr[0:numDigitsLeft]
    if numDigitsLeft == 0:
        digitsLeft = "0"

    digitsLeftInt  = int(digitsLeft)
    digitsRightInt = int(digitsRight)
#    print(num, numSqStr, numDigitsLeft, digitsLeft, numDigitsRight, digitsRight)
    
    
    digitsLeftInt = int(digitsLeft)
    digitsRightInt = int(digitsRight)
    
    if digitsLeftInt + digitsRightInt == num:
        kaprekarNumbers = kaprekarNumbers + str(num) + " "

if kaprekarNumbers == "":
    print("INVALID RANGE")
else:
    print(kaprekarNumbers)        
    #print(numSqStr, numDigitsLeft, digitsLeft, numDigitsRight, digitsRight)