#!/bin/python3

import sys

# John's clothing store has a pile of n loose socks where each sock i is 
# labeled with an integer, ci, denoting its color. He wants to sell as many 
# socks as possible, but his customers will only buy them in matching pairs. 
# Two socks, i and j, are a single matching pair if ci = cj.
#
# Given n and the color of each sock, how many pairs of socks can John sell?
# 
# Input Format
# 
# The first line contains an integer, n, denoting the number of socks. 
# The second line contains n space-separated integers describing the 
# respective values of c0, c1, c2...cn-1.
#
# Output Format
# 
# Print the total number of matching socks that John can sell.

n = int(input().strip())
c = [int(c_temp) for c_temp in input().strip().split(' ')]

sockDict = {}
for sock in c:
    if sock in sockDict:
        sockDict[sock] += 1
    else:
        sockDict[sock] = 1

numPairs = 0
for k, v in sockDict.items():
    numPairs += v // 2

print(numPairs)