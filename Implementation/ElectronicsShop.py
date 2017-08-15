#!/bin/python3

import sys

# Monica wants to buy exactly one keyboard and one USB drive from her favorite 
# electronics store. The store sells n different brands of keyboards and m
# different brands of USB drives. Monica has exactly s dollars to spend, and 
# she wants to spend as much of it as possible (i.e., the total cost of her 
# purchase must be maximal).
#
# Given the price lists for the store's keyboards and USB drives, find and 
# print the amount money Monica will spend. If she doesn't have enough money 
# to buy one keyboard and one USB drive, print -1 instead.
#
# Note: She will never buy more than one keyboard and one USB drive even if 
# she has the leftover money to do so.
# 
# Input Format
# 
# The first line contains three space-separated integers describing the 
# respective values of s (the amount of money Monica has),  (the number of 
# keyboard brands) and m (the number of USB drive brands). 
# The second line contains n space-separated integers denoting the prices of 
# each keyboard brand. 
# The third line contains m space-separated integers denoting the prices of 
# each USB drive brand.
# 
# Output Format
# 
# Print a single integer denoting the amount of money Monica will spend. If she 
# doesn't have enough money to buy one keyboard and one USB drive, print -1 instead.

def getMoneySpent(keyboards, drives, s):
    # Complete this function
    maxSpent = 0
    for kb in keyboards:
        for drive in drives:
            if (kb + drive > maxSpent) and (kb + drive <= s):
                maxSpent = kb + drive
                
    if maxSpent == 0:
        return -1
    else:
        return maxSpent


s,n,m = input().strip().split(' ')
s,n,m = [int(s),int(n),int(m)]
keyboards = list(map(int, input().strip().split(' ')))
drives = list(map(int, input().strip().split(' ')))
#  The maximum amount of money she can spend on a keyboard and USB drive, or -1 
#  if she can't purchase both items
moneySpent = getMoneySpent(keyboards, drives, s)
print(moneySpent)

