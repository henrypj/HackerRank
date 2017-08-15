#!/bin/python3

import sys
"""
# Lilah has a string, S, of lowercase English letters that she repeated 
# infinitely many times.
#
# Given an integer, N, find and print the number of letter a's in the first N
# letters of Lilah's infinite string.
#
# Input Format
#
# The first line contains a single string, S. 
# The second line contains an integer, N.
#
# Constraints
#
# 1 <= |S| <= 100
# 1 <=  N  <= 10**12
# For 25% of the test cases, N <= 10** 6
#
# Output Format 
#
# Print a single integer denoting the number of letter a's in the first N
# letters of the infinite string created by repeating S infinitely many times.
#
# Example 1
#
# Given Input:
# aba
# 10
#
# Output:
# 7
# 
# Explanation:
# The first N=10 letters of the infinite string are abaabaabaa. Because there
# are 7 a's, we print 7 on a new line.
#
# Example 2
#
# Given Input:
# a
# 1000000000000
#
# Output:
# 1000000000000
# 
# Explanation:
# Because all of the first N=1000000000000 letters of the infinite string are a,
# we print 1000000000000 on a new line.
#
# Solution
# 
"""
s = input().strip()
n = int(input().strip())

print((n // len(s) * s.count('a')) + s[0:n % len(s)].count('a'))