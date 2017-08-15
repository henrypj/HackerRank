#!/bin/python3

#a = "zqb"
#lst = list(a)
#lst.sort()
#b = ''.join(lst)

#print(b)

import sys
import random

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
    
n = int(input().strip())
#a = [int(arr_temp) for arr_temp in input().strip().split(' ')]
#b = [int(arr_temp) for arr_temp in input().strip().split(' ')]
a = []
b = []
removeList = []
numRemoved = 0

for x in range(n):
    randNum = random.randint(1, 10**9)
    a.append(randNum)
    randNum = random.randint(1, 10**9)
    b.append(randNum)

#n = 4
#a = [2, 5, 6, 7]
#b = [4, 9, 10, 12]

#print("a => ", a)
#print("b => ", b)
x = 0
while x < len(a):
#    print("x => ", x)
    y = 0
    while y < len(b):
#        print("y => ", y)
#        print("a => ", a[x])
#        print("b => ", b[y])
#        print("gcd => ", gcd(a[x], b[y]))
        if gcd(a[x], b[y]) != 1:
            removeList.append([a[x], b[y]])
            del a[x]
            del b[y]
            numRemoved += 1
            x = -1
            break
        y += 1
    x += 1


print(numRemoved)
print("NumRemoved  => ", numRemoved)
#print("RemovedList => ", removeList)