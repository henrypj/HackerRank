#!/bin/python3

import sys
"""
# Description
# Difficulty: Easy
# 
# Flatland is a country with n cities, m of which have space stations. Each 
# city, c(i), is numbered with a distinct index from 0 to n-1, and each city
# c(i) is connected to city c(i+1) by a bidirectional road that is 1km in length.
#
# For example, if n=5 and cities c(0) and c(4) have space stations, then 
# Flatland looks like this:
# 
# +=====+      +---+      +---+      +---+      +=====+
# |  1  |------| 2 |------| 3 |------| 4 |------|  5  |
# +=====+      +---+      +---+      +---+      +=====+
# 
# For each city, determine its distance to the nearest space station and print
# the maximum of these distances.
#
# Input Format
#
# The first line consists of two space-separated integers, n and m. 
# The second line contains m space-separated integers describing the respective
# indices of each city having a space-station. These values are unordered and 
# unique.
#
# Constraints
#
# 1 <= n <= 10**5
# 1 <= m <= n
# It is guaranteed that there will be at least 1 city with a space station,
# and no city has more than one.
#
# Output Format 
#
# Print an integer denoting the maximum distance that an astronaut in a Flatland
# city would need to travel to reach the nearest space station.
#
# Example 0
#
# Given Input:
# 5 2
# 0 4
#
# Output:
# 2
#
# Explanation:
# This sample corresponds to the example given in the problem statement above. 
# The distance to the nearest space station for each city is listed below:
#
# c(0) has distance 0 km, as it contains a space station.
# c(1) has distance 1 km to the space station in c(0).
# c(2) has distance 2 km to the space stations in c(0) and c(4).
# c(3) has distance 1 km to the space station in c(4).
# c(4) has distance 0 km, as it contains a space station.
#
# We then take the max(0,1,2,1,0) = 2, and print 2 as our answer.
#
# Example 1
#
# Given Input:
# 6 6
# 0 1 2 4 3 5
#
# Explanation:
# In this sample, n = m so every city has a space station and we print 0 as
# our answer.
#
# Output:
# 0
#
# Example 2
# Input:
# 90 11
# 85 44 25 67 20 83 50 88 2 32 16
# 
# Output:
# 8
#
# Example 3
# Input:
# 99992 4
# 90467 18058 99109 48463
#
# Output:
# 21002
#
# Solution
# 
# No help, but did look at 2 test cases
"""
from math import floor

n,m = input().strip().split(' ')
n,m = [int(n),int(m)]
c = [int(c_temp) for c_temp in input().strip().split(' ')]
c.sort()

dist    = 0
maxDist = 0

if m == n:
    pass
elif m == 1:
    maxDist = max(abs(c[0] - 0), abs(c[0] - (n - 1)))
elif m == 2:  # This is wrong
    dist1 = abs(c[0] - 0)
    dist2 = floor(abs((c[0] - c[1]) / 2))
    dist3 = abs(c[1] - (n-1))
    maxDist = max(dist1, dist2, dist3)
else:
    for i in range(m):
        if i == 0:
            dist = c[i] - 0
        elif i < m - 1:
            dist = floor(abs((c[i] - c[i+1]) / 2))
        elif i == m - 1:
            dist = (n - 1) - c[i]

        if dist > maxDist:
            maxDist = dist

print(maxDist)            