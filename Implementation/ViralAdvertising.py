#!/bin/python3

import sys

# https://www.hackerrank.com/challenges/strange-advertising?h_r=next-challenge&h_v=zen

n = int(input().strip())
    
start = 5
numPeople = 0
for i in range(n):
    numPeople += start // 2
    start = (start // 2) * 3
    
print(numPeople)        