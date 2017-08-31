#!/bin/python3
import sys
"""
# Description
# Difficulty: Easy
# 
# Steve has a string, s, consisting of n lowercase English alphabetic letters. 
# In one operation, he can delete any pair of adjacent letters with same value. 
# For example, string "aabcc" would become either "aab" or "bcc" after 1 operation.
#
# Steve wants to reduce s as much as possible. To do this, he will repeat the 
# above operation as many times as it can be performed. Help Steve out by finding
# and printing s's non-reducible form!
#
# Note: If the final string is empty, print Empty String .
#
# Input Format
#
# A single string s.
#
# Constraints
#
# 1 <= n <= 100
#
# Output Format 
#
# If the final string is empty, print Empty String; otherwise, print the final 
# non-reducible string.
#
# Example 0
#
# Given Input:
# aaabccddd
#
# Output:
# abd
#
# Explanation:
# Test Case 0
# Steve can perform the following sequence of operations to get the final string:
# 1. aaabccddd → abccddd
# 2. abccddd → abddd
# 3. abddd → abd
# Thus, we print abd.
#
# Example 1
#
# Given Input:
# baab
#
# Output:
# Empty String
#
# Explanation:
# Test Case 1
# Steve can perform the following sequence of operations to get the final string:
# 1. baab → bb
# 2. bb → Empty String
# Thus, we print Empty String
#
# Solution:
#    
"""
def super_reduced_string(s):
    # Complete this function
    i = 0
    reducedStr = []
    pairsExist = False
    
    while i < len(s):
        if (i == len(s) -1) or (s[i] != s[i+1]):
            reducedStr.extend(s[i])
            i += 1
        else:
            pairsExist = True
            i += 2
            
    if not reducedStr:
        return("Empty String")
    elif pairsExist:
        return(super_reduced_string(reducedStr))
    else:
        return(''.join(reducedStr))

s = input().strip()
result = super_reduced_string(s)
print(result)





































