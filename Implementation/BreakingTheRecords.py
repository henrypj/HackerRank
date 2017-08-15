#!/bin/python3

import sys

def getRecord(s):
    # Complete this function
    high    = 0
    highNum = 0
    low     = 0
    lowNum  = 0
    for i in range(n):
        if i == 0:
            high = s[i]
            low  = s[i]
        else:
            if s[i] > high:
                highNum += 1
                high = s[i]
            if s[i] < low:
                lowNum +=1
                low = s[i]
    return(highNum, lowNum)

n = int(input().strip())
s = list(map(int, input().strip().split(' ')))
result = getRecord(s)
print (" ".join(map(str, result)))
