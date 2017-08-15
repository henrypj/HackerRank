#!/bin/python3

import sys

# Given an array of integers, find and print the maximum number of integers 
# you can select from the array such that the absolute difference between any 
# two of the chosen integers is <= 1.
# 
# Input Format
# 
# The first line contains a single integer, n, denoting the size of the array. 
# The second line contains n space-separated integers describing the respective 
# values of a0, a1,...,an-1.
#
# Constraints
#
# 2 <= n  <= 100
# 0 <= ai <= 100
# 
# Output Format
# 
# A single integer denoting the maximum number of integers you can choose from 
# the array such that the absolute difference between any two of the chosen 
# integers is <= 1.

n = int(input().strip())
a = [int(a_temp) for a_temp in input().strip().split(' ')]

a.sort()
aDict = {}

for num in a:
    if num in aDict:
        aDict[num] += 1
    else:
        aDict[num] = 1
print(aDict)
pairs = [(k, v) for (k, v) in aDict.items()]

maxNum = 0
i = 0
for i in range(len(pairs)-1):
    if (abs(pairs[i][0] - pairs[i+1][0]) <= 1) and ((pairs[i][1] + pairs[i+1][1]) > maxNum):
        maxNum = pairs[i][1] + pairs[i+1][1]

print(max(maxNum, max(aDict.values())))

# A better Solution Below:
# b=[]
# for i in a:
#     b.append(a.count(i)+a.count(i+1))
# print(max(b))
