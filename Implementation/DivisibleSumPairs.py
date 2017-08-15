#!/bin/python3

import sys

n,k = input().strip().split(' ')
n,k = [int(n),int(k)]
a = list(map(int, input().strip().split(' ')))
# write your code here

numPairs = 0
i = 0
while i < len(a):
    x = i + 1
    while x < len(a):
        if (i < x) and ((a[i] + a[x]) % k == 0):
            numPairs += 1
        x += 1
    i += 1

print(numPairs)