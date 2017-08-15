#!/bin/python3

import sys

# You are given a sequence of n integers, p(1),p(2),...,p(n). Each element 
# in the sequence is distinct and satisfies 1 <= p(x) <= n. For each x where
# 1 <= p(x) <= n, find any integer y such that p(p(y)) =x and print the value 
# of y on a new line.
#
# Input Format
#
# The first line contains an integer, n, denoting the number of elements 
# in the sequence. 
# The second line contains n space-separated integers denoting the respective
# values of p(1),p(2),...,p(n).
#
# Constraints
#
# 1 <= n <= 50
# 1 <= p(x) <= 50 where 1 <= x <= n
# Each element in the sequence is unique
#
# Output Format 
#
# For each x from 1 to n, print an integer denoting any valid y satisfying 
# the equation p(p(y)) = x on a new line.
#
# Example
#
# Given Input:
# 3
# 2 3 1
# Output:
# 2
# 3
# 1
# Explanation:
# p(1) = 2, p(2) = 3, p(3) = 1, calculate x from 1 to n
# 1. x = 1 = p(3) = p(p(2)) = p(p(y)), y = 2
# 2. x = 2 = p(1) = p(p(3)) = p(p(y)), y = 3
# 3. x = 3 = p(2) = p(p(1)) = p(p(y)), y = 1
#
# Solution
#
# 

n = int(input().strip())
p = [int(p_temp) for p_temp in input().strip().split(' ')]

for x in range(1, n+1):
    print(p.index(p.index(x) + 1) + 1)
