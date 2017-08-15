#!/bin/python3

import sys
"""
# Description
# Difficulty: Medium
# 
# Given a word w, rearrange the letters of w to construct another word s in 
# such a way that s is lexicographically greater than w. In case of multiple 
# possible answers, find the lexicographically smallest one among them.
#
# Input Format
#
# The first line of input contains t, the number of test cases. Each of the 
# next t lines contains w.
#
# Constraints
#
# 1 <= t <= 10**5
# 1 <= |w| <= 100
#
# Output Format 
#
# For each testcase, output a string lexicographically bigger than w in a 
# separate line. In case of multiple possible answers, print the lexicographically 
# smallest one, and if no answer exists, print no answer.
#
# Example
#
# Given Input:
# 5
# ab
# bb
# hefg
# dhck
# dkhc
#
# Output:
# ba
# no answer
# hegf
# dhkc
# hcdk
#
# Explanation:
#
# Test Case 0:
# There exists only one string greater than ab which can be built by rearrainging
# ab. That is ba.
#
# Test Case 1:
# It is not possible to rearrange bb to get a lexicographically greater string.
#
# Test Case 2:
# hegf is the next string lexicographically greater than hefg.
#
# Test Case 3:
# dhkc is the next string lexicographically greater than dhck.
#
# Test Case 4:
# hcdk is the next string lexicographically greater than dkhc.
#
# Solution
# Took suggestion from the discussion board of looping throug w backwards
# 
"""

    
t = int(input().strip())

def findNextBigger(w):
    wList = list(w)
    biggerFound = False
    if len(set(w)) == 1:
        pass
    else:
        remainingChars = []
        remainingChars.insert(0, wList[-1])
        del wList[-1]
        for i in range(len(wList) - 1, -1, -1):
            if wList[i] >= remainingChars[-1]:
                remainingChars.extend(wList[i])
                del wList[-1]
            else:
                # Find first char in remainingChars that is > current
                biggerFound = True
                for x in range(len(remainingChars)):
                    if remainingChars[x] > wList[i]:
                        # Insert into remainingChars only if > 1 element
                        if len(remainingChars) > 1:
                            remainingChars.insert(0, remainingChars[x])
                            remainingChars[x+1] = wList[i]
                        else:
                            remainingChars.extend(wList[i])
                        del wList[-1]
                        wList.extend(remainingChars)
                        print("".join(wList))
                        return(biggerFound)
    return(biggerFound)

for x in range(t):
    w = input().strip()
    if not findNextBigger(w):
        print("no answer")
        

#def findNextBigger(w):
#    wList = list(w)
#    biggerFound = False
#    if len(set(w)) == 1:
#        pass
#    else:
#        remainingChars = []
#        remainingChars.insert(0, wList[-1])
#        del wList[-1]
#        print(remainingChars)
#        print(wList[-1])
#        print("Looping through word...")
#        for i in range(len(wList) - 1, -1, -1):
#            print("  i                  => ", i)
#            print("  wList[i]           => ", wList[i])
#            print("  remainingChars[-1] => ", remainingChars[-1])
#            if wList[i] >= remainingChars[-1]:
#                print("  Extending remainingChars and deleting last from word")
#                remainingChars.extend(wList[i])
#                del wList[-1]
#                print("  remainingChars => ", remainingChars)
#                print("  wList          => ", wList)
#            else:
#                print("  Should have a bigger...")
#                # Find first char in remainingChars that is > current
#                biggerFound = True
#                for x in range(len(remainingChars)):
#                    print("    Looping through remainingChars...")
#                    print("    x                 => ", x)
#                    print("    remainingChars    => ", remainingChars)
#                    print("    remainingChars[x] => ", remainingChars[x])
#                    print("    wList[i]          => ", wList[i])
#                    if remainingChars[x] > wList[i]:
#                        print("      remainingChars[x] > wList[i]")
#                        # Insert into remainingChars only if > 1 element
#                        if len(remainingChars) > 1:
#                            print("      len of remainingChars > 1")
#                            print("      inserting to remainChars[0] => ", remainingChars[x])
#                            print("      inserting wList[i]          => ", wList[i])
#                            remainingChars.insert(0, remainingChars[x])
#                            remainingChars[x+1] = wList[i]
#                            print("      remainingChars              => ", remainingChars)
#                            print("      wList                       => ", wList)
#                        else:
#                            print("      len of remainingChars <= 1")
#                            remainingChars.extend(wList[i])
#                        del wList[-1]
#                        wList.extend(remainingChars)
#                        print("".join(wList))
#                        return(biggerFound)
#    return(biggerFound)
