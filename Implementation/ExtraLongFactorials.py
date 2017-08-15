#!/bin/python3

import sys
"""
# You are given an integer N. Print the factorial of this number.
#
# N! = N x (N - 1) x (N - 2) x ... x 3 x 2 x 1
#
# Input Format
#
# Input consists of a single integer N, where 1 <= N <= 100.
#
# Constraints
#
#
# Output Format 
#
# Print the factorial of N.
#
# Example
# For an input of 25, you would print 1551210043330985984000000.
#
# Note: Factorials of N > 20 can't be stored even in a 64-bit long long variable.
# Big integers must be used for such calculations. Languages like Java, Python,
# Ruby etc. can handle big integers, but we need to write additional code in C/C++
# to handle huge values.
#
# Solution
"""

n = int(input().strip())

def fact(n):
  if n == 0:
      return 1
  else:
      return n * fact(n-1)

print(fact(n))