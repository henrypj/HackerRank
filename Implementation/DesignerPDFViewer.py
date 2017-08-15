#!/bin/python3

import sys

# When you select a contiguous block of text in a PDF viewer, the selection is 
# highlighted with a blue rectangle. In a new kind of PDF viewer, the selection 
# of each word is independent of the other words; this means that each 
# rectangular selection area forms independently around each highlighted word. 
# For example:
#
#                             Highlighted Text
#                               abc def ghi
#
# In this type of PDF viewer, the width of the rectangular selection area is 
# equal to the number of letters in the word times the width of a letter, 
# and the height is the maximum height of any letter in the word.
#
# Consider a word consisting of lowercase English alphabetic letters, where 
# each letter is 1mm wide. Given the height of each letter in millimeters (mm), 
# find the total area that will be highlighted by blue rectangle in mm**2 when 
# the given word is selected in our new PDF viewer.
# 
# Input Format
# 
# The first line contains 26 space-separated integers describing the respective
# heights of each consecutive lowercase English letter (i.e.h(a), h(b),...,h(z)). 
# The second line contains a single word, consisting of lowercase English 
# alphabetic letters.
#
# Constraints
#
# 1 <= h? <= 7 where ? is an English lowercase word
# Word contains no more than 10 characters
# 
# Output Format
# 
# Print a single integer denoting the area of highlighted rectangle when the 
# given word is selected. The unit of measurement for this is square millimeters
# (mm**2), but you must only print the integer.


h = list(map(int, input().strip().split(' ')))
word = input().strip()
#h = [1, 3, 1, 3, 1, 4, 1, 3, 2, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
#word = "abc"
alphabet = "abcdefghijklmnopqrstuvwxyz"
alphaDict = {}
for i in range(len(h)):
    alphaDict[alphabet[i]] = h[i]
maxHeight = 1    
for letter in word:
    if alphaDict[letter] > maxHeight:
        maxHeight = alphaDict[letter]
print(maxHeight * len(word))