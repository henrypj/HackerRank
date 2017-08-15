#!/bin/python3

import sys

# Anna and Brian order  items at a restaurant, but Anna declines to eat any 
# of the  item (where ) due to an allergy. When the check comes, they decide 
# to split the cost of all the items they shared; however, Brian may have 
# forgotten that they didn't split the  item and accidentally charged Anna 
# for it.
# 
# You are given n, k, the cost of each of the n items, and the total amount 
# of money that Brian charged Anna for her portion of the bill. If the bill 
# is fairly split, print Bon Appetit; otherwise, print the amount of money 
# that Brian must refund to Anna.
# 
# Input Format
# The first line contains two space-separated integers denoting the respective 
# values of n (the number of items ordered) and k (the 0-based index of the item 
# that Anna did not eat).
#  
# The second line contains n space-separated integers where each integer i
# denotes the cost, c[i], of item i (where 0 <= i < n).
#  
# The third line contains an integer, b, denoting the amount of money that 
# Brian charged Anna for her share of the bill.

n,k = input().strip().split(' ')
n,k = [int(n),int(k)]
c = list(map(int, input().strip().split(' ')))
b = int(input().strip())

cTot = sum(c)
bAct = (cTot // 2) - (c[k] // 2)
if b == bAct:
    print("Bon Apetit")
else:
    print(b - bAct)
    