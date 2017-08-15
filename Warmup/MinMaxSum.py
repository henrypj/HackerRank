
import sys


n = int(input().strip())
height = [int(height_temp) for height_temp in input().strip().split(' ')]

maxNum = 
maxHeight = 0
for i in range(n):
    if height[i] > maxHeight:
        maxHeight = height[i]
        maxNum = 1
    elif height[i] == maxHeight:
        maxNum += 1

print()