#!/bin/python3
import sys
"""
# Description
# Difficulty: Easy
# 
# Roy wanted to increase his typing speed for programming contests. So, his 
# friend advised him to type the sentence "The quick brown fox jumps over the 
# lazy dog" repeatedly, because it is a pangram. (Pangrams are sentences 
# constructed by using every letter of the alphabet at least once.)
#
# After typing the sentence several times, Roy became bored with it. So he 
# started to look for other pangrams.
#
# Given a sentence s, tell Roy if it is a pangram or not.
#
# Input Format
#
# Input consists of a string s.
#
# Constraints
#
# Length of s can be at most 10**3 (1 <= |s| <= 10**3) and it may contain spaces,
# lower case and upper case letters. Lower-case and upper-case instances of a 
# letter are considered the same.
#
# Output Format 
#
# Output a line containing pangram if s is a pangram, otherwise output not pangram.
#
# Example 0
#
# Given Input:
# We promptly judged antique ivory buckles for the next prize
#
# Output:
# pangram
#
# Example 1
#
# Given Input:
# We promptly judged antique ivory buckles for the prize
#
# Output:
# not pangram
#
# Explanation:
# In the first test case, the answer is pangram because the sentence contains 
# all the letters of the English alphabet.
#
# Solution: 1
# My initial solution, passes all test cases.
#
# Solution: 2
# After reading the discussion, I learned about using set(), which is an
# unordered collection with no duplicate elements. Using that, the problem
# can be solved by converting the input to a set without spaces and then
# checking to see if the lenght is equal to 26. This would not work if the
# input string had special characters though, unless those too were ignored.
#
"""
##############
# SOLUTION 1 #
##############
import string
s = input().strip().lower()
pangramFound = False
charList = []

for char in s:
    if char.isalpha() and char not in charList:
        charList.append(char)
        sortedCharList = sorted(charList)
        charStr = ''.join(sortedCharList)
        if charStr == string.ascii_lowercase:
            pangramFound = True
            break

if pangramFound:
    print("pangram")
else:
    print("not pangram")
    
###############
# SOLUTION 2a #
###############
#from collections import Counter
#print("pangram" if len(Counter(input().lower().replace(' ',''))) == 26 else "not pangram")

###############
# SOLUTION 2B #
###############
#ALPHABET_SIZE = 26
#chars = set(input().lower().replace(' ', ''))
#
#if len(chars) == ALPHABET_SIZE:
#    print('pangram')
#else:
#    print('not pangram')