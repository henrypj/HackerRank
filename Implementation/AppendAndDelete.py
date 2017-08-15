#!/bin/python3

import sys
"""
# You have a string, s, of lowercase English alphabetic letters. You can 
# perform two types of operations on s:
#
# 1. Append a lowercase English alphabetic letter to the end of the string.
# 2. Delete the last character in the string. Performing this operation on 
#    an empty string results in an empty string.
#
# Given an integer, k, and two strings, s and t, determine whether or not you
# can convert s to t by performing exactly k of the above operations on s. If 
# it's possible, print Yes; otherwise, print No.
#
# Input Frmat
#
# The first line contains a string, s, denoting the initial string. 
# The second line contains a string, t, denoting the desired final string. 
# The third line contains an integer, k, denoting the desired number of operations.
#
# Constraints
#
# 1 <= |s| <= 100
# 1 <= |t| <= 100
# 1 <=  k  <= 100
#
# Output Format 
#
# Print Yes if you can obtain string t by performing exactly k operations on s; 
# otherwise, print No.
#
# Example 1
#
# Given Input:
# hackerhappy
# hackerrank
# 9
#
# Output:
# Yes
#
# Explanation:
# We perform 5 delete operations to reduce string s to hacker. Next, we perform
# 4 append operations (i.e., r, a, n, and k), to get hackerrank. Because we were
# able to convert s to t by performing exactly k operations, we print Yes.
#
# Example 2
# 
# Sample Input
# aba
# aba
# 7
#
# Sample Output
#
# Yes
#
# Explanation:
# We perform 4 delete operations to reduce string s to the empty string (recall
# that, though the string will be empty after 3 deletions, we can still perform
# a delete operation on an empty string to get the empty string). Next, we 
# perform 3 append operations (i.e., a, b, and a). Because we were able to 
# convert s to t by performing exactly k=7 operations, we print Yes
#
# Solution
# See below...Needed help
"""

s = input().strip()
t = input().strip()
k = int(input().strip())

if k >= len(s) + len(t):
    print("Yes")
else:
    charsInCommon = 0
    for i in range(length):
        if s[i] == t[i]:
            charsInCommon += 1
        else:
            break

    # Find total number of uncommon chars
    uncommonChars = len(s) - charsInCommon + len(t) - charsInCommon
    
    # Conditions which would lead to Yes
    # 1. k = uncommonChars
    if k == uncommonChars:
        print("Yes")
    # 2. k > uncommonChars and both k and uncommonChars are odd
    elif k > uncommonChars and k % 2 != 0 and uncommonChars % 2 != 0:
        print("Yes")
    # 3. k > uncommonChars and both k and uncommonChars are even
    elif k > uncommonChars and k % 2 == 0 and uncommonChars % 2 == 0:
        print("Yes")
    else:
        print("No")


























