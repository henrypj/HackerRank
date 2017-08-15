#!/bin/python3

import sys

def solve(n, s, d, m):
    # Complete this function
    totPieces = 0
    
    for i in range(len(s)-m + 1):
        if sum(s[i:i+m]) == d:
            totPieces += 1
    return totPieces
        
n = int(input().strip())
s = list(map(int, input().strip().split(' ')))
d, m = input().strip().split(' ')
d, m = [int(d), int(m)]
result = solve(n, s, d, m)
print(result)
