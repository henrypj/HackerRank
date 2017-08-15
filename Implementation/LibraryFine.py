#!/bin/python3

import sys
"""
# Your local library needs your help! Given the expected and actual return 
# dates for a library book, create a program that calculates the fine (if any).
# The fee structure is as follows:
#
# 1. If the book is returned on or before the expected return date, no fine will 
#    be charged (i.e.: fine = 0).
#
# 2. If the book is returned after the expected return day but still within the
#    same calendar month and year as the expected return date, 
#    fine = 15 Hackos X (the number of days late).
#
# 3. If the book is returned after the expected return month but still within 
#    the same calendar year as the expected return date, the 
#    fine = 500 Hackos x (the number of months late).
#
# 4. If the book is returned after the calendar year in which it was expected, 
#    there is a fixed fine of 10,000 Hackos.
#
# Input Frmat
#
# The first line contains 3 space-separated integers denoting the respective
# day, month, and year on which the book was actually returned. 
#
# The second line contains 3 space-separated integers denoting the respective 
# day, month, and year on which the book was expected to be returned (due date).
#
# Constraints
#
# 1 <= D <= 31
# 1 <= M <= 12
# 1 <= Y <= 3000
# It is guaranteed that each date will be valid Gregorian calendar dates.
#
# Output Format 
#
# Print a single integer denoting the library fine for the book received as input.
#
# Example 1
#
# Given Input:
# 9 6 2015
# 6 6 2015
#
# Output:
# 45
#
# Explanation:
# Given the following return dates: 
# Actual:   Da = 9, Ma = 6, Ya = 2015  
# Expected: De = 6, Me = 6, Ye = 2015
# 
# Because Ye = Ya, we know it is less than a year late. 
# Because Me = Ma, we know it's less than a month late. 
# Because De < Da, we know that it was returned late (but still within the 
# same month and year).
#
# Per the library's fee structure, we know that our fine will be 15 Hackos x
# (# days late). We then print the result of 15 x (Da - De) = 15 x (9 - 6) =
# 45 as our output.
#
# Solution
# 
"""
# dmy1 = Actual
# dmy2 = Expected
d1,m1,y1 = input().strip().split(' ')
d1,m1,y1 = [int(d1),int(m1),int(y1)]
d2,m2,y2 = input().strip().split(' ')
d2,m2,y2 = [int(d2),int(m2),int(y2)]

fine = 0
if y1 > y2:
    fine = 10000
elif y1 == y2 and m1 > m2: 
    fine = 500 * (m1 - m2)
elif y1 == y2 and m1 == m2 and d1 > d2:
    fine = 15 * (d1 - d2)

print(fine)
    
