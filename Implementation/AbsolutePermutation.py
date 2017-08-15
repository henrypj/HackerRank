#!/bin/python3
import sys
"""
# Description
# Difficulty: Medium
# 
# We define P to be a permutation of the first N natural numbers in the range 
# [1, N]. Let pos(i) denote the position of i in permutation P (please use 1-based
# indexing).
#
# P is considered to be an absolute permutation if abs(pos(i) - i) = K holds true
# for every i = [1, N].
#
# Given N and K, print the lexicographically smallest absolute permutation, P; 
# if no absolute permutation exists, print -1.
#
# Input Format
#
# The first line of input contains a single integer, T, denoting the number of 
# test cases. 
# Each of the T subsequent lines contains 2 space-separated integers describing
# the respective N and K values for a test case.
#
# Constraints
#
# 1 <= T <= 10
# 1 <= N <= 10**5
# 0 <= K <= N
#
# Output Format 
#
# On a new line for each test case, print the lexicographically smallest absolute
# permutation; if no absolute permutation exists, print -1
#
# Example 0
#
# Given Input:
# 3
# 2 1
# 3 0
# 3 2
#
# Output:
# 2 1
# 1 2 3
# -1
#
# Explanation:
# Test Case 0
#                          +---+   +---+
#                 Position | 1 |   | 2 |
#                          +---+   +---+
#
#                          +---+   +---+
#              Permutation | 2 |   | 1 |
#                          +---+   +---+
#
#                          +---+   +---+
#      Absolute Difference | 1 |   | 1 |
#                          +---+   +---+
#
# Test Case 1
#                          +---+   +---+   +---+
#                 Position | 1 |   | 2 |   | 3 |
#                          +---+   +---+   +---+
#
#                          +---+   +---+   +---+
#              Permutation | 1 |   | 2 |   | 3 |
#                          +---+   +---+   +---+
#
#                          +---+   +---+   +---+
#      Absolute Difference | 0 |   | 0 |   | 0 |
#                          +---+   +---+   +---+
#
# Test Case 3
# No absolute permutation exists, so we print -1 on a new line.
#
# Solution:
#    
# My solution 1 below is functionally correct, but timed out for all test
# cases except test case 0.    
# 
# Based on reading the discussions, there is actually no need to calculate
# the permutations (this is causing the timeouts). Simple solution based
# on the following:
#
# 1. If n is even, (n % k == 0) lets you know that there is a valid permutation
#    or if you should just return -1.
#
# 2. If k == 0, just return 1...n
#
# 3. If n is an odd number > 0, return -1
# 
# My Solution 2 is based on that, but 
"""
##############
# SOLUTION 3 #
##############

#for _ in range(int(input().strip())):
#    n, k = [int(x) for x in input().strip().split(' ')]
#    if k != 0 and n % k != 0:
#        print(-1)
#        continue
#
#    arr = [None] * (n+1) # initialize iterable
#    for i in range(1,len(arr)):
#        if arr[i] is None:
#            arr[i] = i + k
#            arr[i+k] = i
#
#    print(' '.join([str(j) for j in arr[1:]]))
##############
# SOLUTION 2 #
##############
t = int(input().strip())
for a0 in range(t):
    n,k = input().strip().split(' ')
    n,k = [int(n),int(k)]

    usedNums = []
    if k == 0:
        for i in range(1, n+1):
            print(i, end=" ")
    elif n % 2 != 0:
        print("-1")
    elif (n % 2 == 0) and (n % k == 0) and ((n / k) % 2 == 0):   # Valid perms
        for i in range(1, n+1):
            if i - k > 0 and i - k not in usedNums:
                print(i - k, end=" ")
                usedNums.append(i - k)
            else:
                print(i + k, end=" ")
                usedNums.append(i + k)
    else:
        print("-1")
    
    print("\r")

#1 2 3 4 5 6 7 8   1
#2 1 4 3 6 5 8 7
#
#1 2 3 4 5 6 7 8   2
#3 4 1 2 7 8 5 6
#
#1 2 3 4 5 6 7 8   4
#5 6 7 8 1 2 3 4


##############
# SOLUTION 1 #
##############
#
#def perm1(lst):
#    if len(lst) == 0:
#        return []
#    elif len(lst) == 1:
#        return [lst]
#    else:
#        l = []
#        for i in range(len(lst)):
#            x = lst[i]
#            xs = lst[:i] + lst[i+1:]
#            for p in perm1(xs):
#                l.append([x]+p)
#        return l
#
#t = int(input().strip())
#for a0 in range(t):
#    n,k = input().strip().split(' ')
#    n,k = [int(n),int(k)]
#    
#    listN = []
#    resultSet = []
#
#    for i in range(n):
#        listN.append(i + 1)
#    print(listN)    
#    
#    for p in perm1(listN):
#        i = 1
#        absoluteP = True
#        for char in p:
#            if abs(int(char) - i) == k:
#                i += 1
#            else:
#                absoluteP = False
#                break
#        if absoluteP:
#            resultSet.append(p)
#
#    if len(resultSet) == 0:
#        print("-1")
#    elif len(resultSet) == 1:
#        for p in resultSet:
#            print(' '.join(str(x) for x in p))
#    else:
#        i = 1
#        smallest = ""
#        for p in resultSet:
#            if i == 1 or p < smallest:
#                smallest = p
#            i += 1
#
