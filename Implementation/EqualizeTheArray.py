#!/bin/python3

import sys
"""
# Karl has an array of n integers defined as A = a(0), a(1),...,a(n-1). In one 
# operation, he can delete any element from the array.
#
# Karl wants all the elements of the array to be equal to one another. To do 
# this, he must delete zero or more elements from the array. Find and print 
# the minimum number of deletion operations Karl must perform so that all the 
# array's elements are equal.
#
# Input Format
#
# The first line contains an integer, n, denoting the number of elements in array A. 
# The next line contains n space-separated integers where element i corresponds 
# to array element a(i) (0 <= i < n).
#
# Constraints
#
# 1 <=  n   <= 100
# 1 <= a(i) <= 100
#
# Output Format 
#
# Print a single integer denoting the minimum number of elements Karl must 
# delete for all elements in the array to be equal
#
# Example 0
#
# Given Input:
# 5
# 3 3 2 1 3
#
# Output:
# 2
#
# Explanation:
# Array A = [3,3,2,1,3]. If we delete a(2) = 2 and a(3) = 1, all of the elements
# in the resulting array, A' = [3,3,3], will be equal. Deleting these 2 elements
# is minimal because our only other options would be to delete 4 elements to get
# an array of either [1] or [2]. Thus, we print 2 on a new line, as that is the
# minimum number of deletions resulting in an array where all elements are equal.
#
# Solution
# The following solution works for all test cases...
# print(n - max([A.count(t) for t in set(A)]))

"""

n = int(input().strip())
A = list(map(int, input().split()))

aDict = {}

for i in A:
    aDict[i] = aDict.get(i,0) + 1

print(n - max(aDict.items())[1])