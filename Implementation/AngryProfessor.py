#!/bin/python3

import sys

# A Discrete Mathematics professor has a class of N students. Frustrated with 
# their lack of discipline, he decides to cancel class if fewer than K students
# are present when class starts.
#
# Given the arrival time of each student, determine if the class is canceled.
# 
# Input Format
# 
# The first line of input contains T, the number of test cases.
#
# Each test case consists of two lines. The first line has two space-separated
# integers, N (students in the class) and K (the cancelation threshold). The 
# second line contains N space-separated integers (a1, a2,...,aN) describing 
# the arrival times for each student.
#
# Note: Non-positive arrival times (a(i) <= 0) indicate the student arrived 
# early or # on time; positive arrival times (a(i) > 0) indicate the student 
# arrived a(i) minutes late.
#
# Constraints
#
# 1 <= T <= 10
# 0 <= N <= 1000
# 1 <= K <= N
# -100 <= a(i) <= 100 where i in [1,N]
# 
# Output Format
# 
# For each test case, print the word YES if the class is canceled or NO 
# if it is not.
#
# Note 
# If a student arrives exactly on time , the student is considered to have 
# entered before the class started.

t = int(input().strip())
for a0 in range(t):
    n,k = input().strip().split(' ')
    n,k = [int(n),int(k)]
    a = [int(a_temp) for a_temp in input().strip().split(' ')]
    
    numStudents = sum(1 for i in a if i <= 0)
    print("YES" if numStudents < k else "NO")
    