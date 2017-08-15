#!/bin/python3

import sys
"""
# Description
# Difficulty: Easy
# 
# Erica wrote an increasing sequence of n numbers (a(0), a(1),...,a(n-1)) in her
# notebook. She considers a triplet (a(i),a(j),a(k)) to be beautiful if:
#
# i < j < k
# a[j] = a[i] = a[k] - a[j] = d
#
# Given the sequence and the value of d, can you help Erica count the number of
# beautiful triplets in the sequence?.
#
# Input Format
#
# The first line contains 2 space-separated integers, n (the length of the 
# sequence) and d (the beautiful difference), respectively. 
# The second line contains n space-separated integers describing Erica's 
# increasing sequence, a(0), a(1),...,a(n-1).
#
# Constraints
#
# 1 <= n <= 10**4
# 1 <= d <= 20
# 0 <= a(i) <= 2 x 10**4
# a(i) > a(i-1) for 0 < i <= n-1
#
# Output Format 
#
# Print a single line denoting the number of beautiful triplets in the sequence.
#
# Example
#
# Given Input:
# 7 3
# 1 2 4 5 7 8 10
#
# Output:
# 3
#
# Explanation:
#
# Our input sequence is 1,2,4,5,7,8,10, and our beautiful difference d=3. There
# are many possible triplets a(i),a(j),a(k), but our only beautiful triplets are
# (1,4,7), (4,7,10) and (2,5,8). Please see the equations below:
#
# 7-4  = 4-1 = 3 = d
# 10-7 = 7-4 = 3 = d
# 8-5  = 5-2 = 3 = d
#
# Solution
# 
"""
n,d = input().strip().split(' ')
n,d = [int(n),int(d)]
a = [int(a_temp) for a_temp in input().strip().split(' ')]

numTriplets = 0
for i in range(n):
    for j in range(i+1, n):
        if a[j] - a[i] == d:
            # Found one pair of the beautiful triplet, check for 2nd  pair
            for k in range(j+1, n):
                if a[k] - a[j] == d:
                    # Found second pair of the beautiful triplet
                    numTriplets += 1
                elif a[k] - a[j] > d:
                    break
        elif a[j] - a[i] > d:
            break
            
print(numTriplets)