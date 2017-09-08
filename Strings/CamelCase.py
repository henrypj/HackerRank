#!/bin/python3
import sys
"""
# Description
# Difficulty: Easy
# 
# Alice wrote a sequence of words in CamelCase as a string of letters, s, having the following 
# properties:
#
# - It is a concatenation of one or more words consisting of English letters.
# - All letters in the first word are lowercase.
# - For each of the subsequent words, the first letter is uppercase and rest of the letters are
#   lowercase.
#
# Given s, print the number of words in s on a new line.
#
# Input Format
#
# A single line containing the string s.
#
# Constraints
#
# 1 <= |s| <= 10**5
#
# Output Format 
#
# Print the number of words in string s.
#
# Example 0
#
# Given Input:
# saveChangesInTheEditor
#
# Output:
# 5
#
# Explanation:
# Test Case 0
# String s contains 5 words, 1) save, 2) Changes, 3) In, 4) The, 5) Editor, thus we print 5
# on a new line.
#
# Solution:
#    
"""
s = input().strip()
print(1 + sum(1 for c in s if c.isupper()))