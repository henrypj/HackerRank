#!/bin/python3

import sys

# John Watson performs an operation called a right circular rotation on an 
# array of integers, a(0), a(1),...,a(n-1). After performing one right circular
# rotation operation, the array is transformed from  a(0), a(1),...a(n-1) to 
# a(n-1), a(0), a(1),...,a(n-2).
#
# Watson performs this operation k times. To test Sherlock's ability to 
# identify the current element at a particular position in the rotated array, 
# Watson asks q queries, where each query consists of a single integer, m, for 
# which you must print the element at index m in the rotated array (i.e., the 
# value of a(m)).
#
# Input Format
#
# The first line contains 3 space-separated integers, n, k, and q, respectively. 
# The second line contains n space-separated integers, where each integer i 
# describes array element a(i) (where 0 <= i <n). 
# Each of the q subsequent lines contains a single integer denoting m.
#
# Constraints
#
# 1 <= n <= 10**5
# 1 <= a(i) <= 10**5
# 1 <= k <= 10**5
# 1 <= q <= 500
# 0 <= m <= n - 1
#
# Output Format 
#
# For each query, print the value of the element at index m of the rotated 
# array on a new line.
#
# Solution
#
# Needed to add k = k % n when k > n

n,k,q = input().strip().split(' ')
n,k,q = [int(n),int(k),int(q)]
a = [int(a_temp) for a_temp in input().strip().split(' ')]
if k > n:
    k = k % n
for a0 in range(q):
    m = int(input().strip())
    aRot = a[len(a)-k:] + a[:-k]
    print(aRot[m]) 