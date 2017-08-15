#!/bin/python3
import sys
"""
# Description
# Difficulty: Medium
# 
# Given a 2D array of digits, try to find the occurrence of a given 2D pattern
# of digits. For example, consider the following 2D matrix:
#
# 1234567890
# 0987654321
# 1111111111
# 1111111111
# 2222222222
#
# Assume we need to look for the following 2D pattern:
#
# 876543
# 111111
# 111111
#
# If we scan through the original array, we observe that the 2D pattern begins
# at the second row and the third column of the larger grid (the 8 in the second
# row and third column of the larger grid is the top-left corner of the pattern
# we are searching for).
#
# So, a 2D pattern of P digits is said to be present in a larger grid G, if the
# latter contains a contiguous, rectangular 2D grid of digits matching with the
# pattern P, similar to the example shown above.
#
# Input Format
#
# The first line contains an integer, T, which is the number of test cases. T 
# test cases follow, each having a structure as described below: 
# The first line contains two space-separated integers, R and C, indicating the
# number of rows and columns in the grid G, respectively. 
# This is followed by R lines, each with a string of C digits, which represent
# the grid G. 
# The following line contains two space-separated integers, r and c, indicating
# the number of rows and columns in the pattern grid P. 
# This is followed by r lines, each with a string of c digits, which represent
# the pattern P.
#
# Constraints
#
# 1 <= T <= 5
# 1 <= R,r,C,c <= 1000
# 1 <= r <= R
# 1 <= c <= C
#
# Output Format 
#
# Display 'YES' or 'NO', depending on whether (or not) you find that the larger
# grid G contains the rectangular pattern P. The evaluation will be case sensitive.
#
# Example 0
#
# Given Input:
# 2
# 10 10
# 7283455864
# 6731158619
# 8988242643
# 3830589324
# 2229505813
# 5633845374
# 6473530293
# 7053106601
# 0834282956
# 4607924137
# 3 4
# 9505
# 3845
# 3530
# 15 15
# 400453592126560
# 114213133098692
# 474386082879648
# 522356951189169
# 887109450487496
# 252802633388782
# 502771484966748
# 075975207693780
# 511799789562806
# 404007454272504
# 549043809916080
# 962410809534811
# 445893523733475
# 768705303214174
# 650629270887160
# 2 2
# 99
# 99
#
# Output:
# YES
# NO
#
# Explanation:
# The first test case contains the pattern, the second test case does not.
#
# Other Test Cases:
#R=10
#C=10
#G=['7283455864', '6731158619', '8988242643', '3830589324', '2229505813', '5633845374', '6473530293', '7053106601', '0834282956', '4607924137']
#r=3
#c=4
#P=['9505', '3845', '3530']

#R=4
#C=6
#G=['123412', '561212', '123634', '781288']
#r=2
#c=2
#P=['12', '34']

#R=4
#C=6
#G=['123456','567890','234567','194729']
#r=4
#c=4
#P=['1234','5678','2345','4729']

#R=5
#C=15
#G=['111111111111111','111111111111111','111111011111111','111111111111111','111111111111111']
#r=3
#c=5
#P=['11111','11111','11110']

R=4
C=5
G=['1211','2112','3434','7878']
r=1
c=2
P=['21']

# Solution
# Initial solution had runtime error on test cases 7,9,15 and wrong on test
# case 8
# Solution #2 works for all test cases
"""
t = int(input().strip())
for a0 in range(t):
    R,C = input().strip().split(' ')
    R,C = [int(R),int(C)]
    G = []
    G_i = 0
    for G_i in range(R):
       G_t = str(input().strip())
       G.append(G_t)
    r,c = input().strip().split(' ')
    r,c = [int(r),int(c)]
    P = []
    P_i = 0
    for P_i in range(r):
       P_t = str(input().strip())
       P.append(P_t)

##################
#   SOLUTION 2   #
##################
def checkPattern(row, col):
    # First row of P was found in G at row, col. This checks the rest of the
    # rows in P to see if they are in G at row + i and column col.
    if row + r - 1 > R:     # Not enough rows left in G to have P
        return False
    
    for i in range(1, r):
        result = G[row + i].find(P[i], col, col + c)
        if result < 0:
            return False
    return True

foundPattern = False
for currRow in range(R):
    currCol = 0
    while currCol < C - 1 and not foundPattern:
        startCol = G[currRow].find(P[0], currCol)   # Check if first row of P is in G
        if startCol >= 0:
            if checkPattern(currRow, startCol):
                foundPattern = True
            else:
                rowsFound = 0
                currCol += 1
        else:
            break
                    
    if foundPattern:
        break        

if foundPattern:
    print("YES")
else:
    print("NO")                

##################
#   SOLUTION 1   #
##################
#foundPattern = False
#for i in range(R):
#    start = G[i].find(P[0])
#    print("i     => ", i)
#    print("start => ", start)
#    if start >= 0:
#        rowsFound = 1
#        print("rowsFound => ", rowsFound)
#        if r == 1:
#            foundPattern = True
#        else:
#            # Check if pattern rows can fit in remainin rows
#            if (R - i) > (r - 1):
#                print("There are ", R-i, " rows remaining and ", r-1," in pattern.")
#                for j in range(1, r):
#                    print("j    => ", j)
#                    print("G[i+j] => ", G[i+j])
#                    print("P[j]   => ", P[j])
#                    print("start  => ", start)
#                    if G[i + j].find(P[j]) == start:
#                    #if P[j] in G[i + j] and G[i + j].find(P[j]) == start:
#                        print("Found pattern row in Grid, incrementing rowsFound")
#                        rowsFound += 1
#                    #else:
#                    #    break
#                
#                print("rowsFound => ", rowsFound)
#                if rowsFound == r:
#                    foundPattern = True
#                    break
#                #else:
#                #    break
#        
#if foundPattern:
#    print("YES")
#else:
#    print("NO")        
#    
