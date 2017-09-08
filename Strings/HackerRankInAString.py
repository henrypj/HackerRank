#!/bin/python3
import sys
"""
# Description
# Difficulty: Easy
# 
# We say that a string, s, contains the word hackerrank if a subsequence of the
# characters in s spell the word hackerrank. For example, haacckkerrannkk does 
# contain hackerrank, but haacckkerannk does not (the characters all appear in 
# the same order, but it's missing a second r).
#
# More formally, let p(0),p(1)...p(9) be the respective indices of h, a, c, k, 
# e, r, r, a, n, k in string s. If p(0) < p(1) < p(2) < ... < p(9) is true, 
# then s contains hackerrank.
#
# You must answer n queries, where each query consists of a string, s. For each
# query, print YES on a new line if contains hackerrank; otherwise, print NO 
# instead.
#
# Input Format
#
# The first line contains an integer denoting q (the number of queries). 
# Each line of the q subsequent lines contains a single string denoting s.
#
# Constraints
#
# 2 <= q <= 10**2
# 10 <= len(s) <= 10**4
#
# Output Format 
#
# For each query, print YES on a new line if s(i) contains hackerrank; otherwise, 
# print NO instead.
#
# Example 0
#
# Given Input:
# 2
# hereiamstackerrank
# hackerworld
#
# Output:
# YES
# NO
#
# Explanation:
# Test Case 0
# We perform the following q=2 queries:
#
#         _        _________
# 1. s =  hereiamstackerrank
#    The characters of hackerrank are bolded in the string above. Because the 
#    string contains all the characters in hackerrank in the same exact order 
#    as they appear in hackerrank, we print YES on a new line.
#
#        ______  _
# 2. s = hackerworld does not contain the last three characters of hackerrank, 
#    so we print NO on a new line.
#
# Solution:
#    
"""
q = int(input().strip())
for a0 in range(q):
    s = input().strip()
    # your code goes here
    
    hackerrank = "hackerrank"
    letterIndex = 0
    found = False
    
    for i in range(len(s)):
        if s[i] == hackerrank[letterIndex]:
            letterIndex += 1
            if letterIndex > 9:  # hackerrank found
                found = True
                break

    if found:
        print("YES")
    else:
        print("NO")