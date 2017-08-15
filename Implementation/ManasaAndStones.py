#!/bin/python3
import sys
"""
# Description
# Difficulty: Easy
# 
# Manasa is out on a hike with friends. She finds a trail of stones with numbers
# on them. She starts following the trail and notices that two consecutive stones
# have a difference of either a or b. Legend has it that there is a treasure 
# trove at the end of the trail and if Manasa can guess the value of the last 
# stone, the treasure would be hers. Given that the number on the first stone 
# was 0, find all the possible values for the number on the last stone.
#
# Note: The numbers on the stones are in increasing order.
#
# Input Format
#
# The first line contains an integer T, i.e. the number of test cases. T test 
# cases follow; each has 3 lines. The first line contains n (the number of 
# stones). The second line contains a, and the third line contains b.
#
# Constraints
#
# 1 <= T <= 10
# 1 <= n,a,b <= 10**3
#
# Output Format 
#
# Space-separated list of numbers which are the possible values of the last 
# stone in increasing order.
#
# Example 0
#
# Given Input:
# 2
# 3
# 1
# 2
# 4
# 10
# 100
#
# Output:
# 2 3 4
# 30 120 210 300
#
# Explanation:
# All possible series for the first test case are given below:
#
# 1. 0, 1, 2
# 2. 0, 1, 3
# 3. 0, 2, 3
# 4. 0, 2, 4
# 
# Hence the answer is 2 3 4
#
# Series with different number of final steps for second test case are the following:
# 
# 1. 0, 10, 20, 30
# 2. 0, 10, 20, 120
# 3. 0, 10, 110, 120
# 4. 0, 10, 110, 210
# 5. 0, 100, 110, 120
$ 6. 0, 100, 110, 210
# 7. 0, 100, 200, 210
# 8. 0, 100, 200, 300
#
# Hence the answer is 30 120 210 300
#
# Solution
# 
"""
from itertools import permutations
#t = int(input().strip())   # Number of test cases
#n = int(input().strip())   # Number of stones
#a = int(input().strip())   # Distance a
#b = int(input().strip())   # Distance b
n = 4
a = 10
b = 100

def makeCounter_rec(base):
    def incDigit(num, pos):
        new = num[:]
        if(num[pos] == base - 1):
            new[pos] = 0
            if(pos < len(num) - 1):    return incDigit(new, pos + 1)
        else:
            new[pos] = new[pos] + 1
        return new

    def inc(num): return incDigit(num, 0)
    return inc

base = 2
inc = makeCounter_rec(base)
n = [0,0]
print(n)
for i in range(base ** len(n)):
    n = inc(n)
    print(n)


































