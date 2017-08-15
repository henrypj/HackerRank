#!/bin/python3

import sys
"""
# Watson gives two integers (A and B) to Sherlock and asks if he can count the
# number of square integers between A and B (both inclusive).
#
# Note: A square integer is an integer which is the square of any integer. 
# For example, 1, 4, 9, and 16 are some of the square integers as they are 
# squares of 1, 2, 3, and 4, respectively.
#
# Input Frmat
#
# The first line contains T, the number of test cases. T test cases follow, 
# each in a new line. 
# Each test case contains two space-separated integers denoting A and B.
#
# Constraints
#
# 1 <= T <= 100
# 1 <= A <= B <= 10**9
#
# Output Format 
#
# For each test case, print the required answer in a new line.
#
# Example 1
#
# Given Input:
# 2
# 3 9
# 17 24
#
# Output:
# 2
# 0
#
# Explanation:
# Test Case #00: In range [3,9], 4 and 9 are the two square numbers. 
# Test Case #01: In range [17,24], there are no square numbers.
#
# Solution
# 
"""

from math import floor, ceil, sqrt

t = int(input().strip())
for a0 in range(t):
    a, b = input().strip().split(' ')
    a, b = [int(a), int(b)]
    
    count = 0
    start = floor(sqrt(a))
    while (start * start <= b):
        sq = (start * start)
        if(sq >= a and sq <= b):
            count += 1
            a = sq
        start += 1
    print(count)


#    def isqrt(n):
#        i = int(math.sqrt(n) + 0.5)
#        if i**2 == n:
#            return i
#        raise ValueError('input was not a perfect square')#
#    numSquares = 0
#    for i in range(a,b+1):
#        x = isqrt(i)
#        if x != 0:
#            numSquares += 1
#    print(numSquares)

























