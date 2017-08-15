#!/bin/python3

import sys
from operator import itemgetter

n = int(input().strip())
types = list(map(int, input().strip().split(' ')))
# your code goes here
typeNums = {}
for typ in types:
    if typ in typeNums:
        typeNums[typ] += 1
    else:
        typeNums[typ] = 1                
typeNumsList = (sorted(typeNums.items(), key=itemgetter(1), reverse=True))

mostCommon = [(99,0)]
for i in range(len(typeNumsList)):  
    if typeNumsList[i][1] >= mostCommon[0][1] and typeNumsList[i][0] < mostCommon[0][0]:
        mostCommon = [(typeNumsList[i][0], typeNumsList[i][1])]
        
print(mostCommon[0][0])