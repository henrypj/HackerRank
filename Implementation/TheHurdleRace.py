#!/bin/python3

import sys

# Dan is playing a video game in which his character competes in a hurdle race 
# by jumping over n hurdles with heights h(0), h(1),...,h(n-1). He can initially
# jump a maximum height of k units, but he has an unlimited supply of magic 
# beverages that help him jump higher! Each time Dan drinks a magic beverage, 
# the maximum height he can jump during the race increases by 1 unit.
#
# Given n, k, and the heights of all the hurdles, find and print the minimum 
# number of magic beverages Dan must drink to complete the race.
# 
# Input Format
# 
# The first line contains two space-separated integers describing the respective
# values of n (the number of hurdles) and k (the maximum height he can jump 
# without consuming any beverages). 
# The second line contains n space-separated integers describing the respective
# values of h(0), h(1),...,h(n-1).
#
# Constraints
#
# 1 <= n, k <= 100
# 1 <= h(i) ,= 100
# 
# Output Format
# 
# Print an integer denoting the minimum number of magic beverages Dan must drink 
# to complete the hurdle race.


n,k = input().strip().split(' ')
n,k = [int(n),int(k)]
height = list(map(int, input().strip().split(' ')))
# your code goes here
maxHeight = max(height)
if k >= maxHeight:
    print(0)
else:
    print(maxHeight - k)