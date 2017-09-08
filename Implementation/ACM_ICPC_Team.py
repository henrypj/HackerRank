#!/bin/python3
import sys
"""
# Description
# Difficulty: Easy
# 
# You are given a list of N people who are attending ACM-ICPC World Finals. Each
# of them are either well versed in a topic or they are not. Find out the maximum
# number of topics a 2-person team can know. And also find out how many teams can
# know that maximum number of topics.
#
# Note Suppose a, b, and c are three different people, then (a,b) and (b,c) are
# counted as two different teams.
#
# Input Format
#
# The first line contains two integers, N and M, separated by a single space, 
# where N represents the number of people, and M represents the number of topics.
# N lines follow.
#
# Each line contains a binary string of length M. If the i'th line's j'th character
# is 1, then the i'th person knows the j'th topic; otherwise, he doesn't know the 
# topic.
#
# Constraints
#
# 2 <= N <= 500
# 1 <= M <= 500
#
# Output Format 
#
# On the first line, print the maximum number of topics a 2-person team can know. 
# On the second line, print the number of 2-person teams that can know the maximum
# number of topics.
#
# Example 0
#
# Given Input:
# 4 5
# 10101
# 11100
# 11010
# 00101
#
# Output:
# 5
# 2
#
# Explanation:
# (1, 3) and (3, 4) know all the 5 topics. So the maximal topics a 2-person team
# knows is 5, and only 2 teams can achieve this.
#
# Solution:
# 
"""
##############
# SOLUTION 1 #
##############
n,m = input().strip().split(' ')
n,m = [int(n),int(m)]
topic = []
topic_i = 0
for topic_i in range(n):
   topic_t = str(input().strip())
   topic.append(topic_t)

numTeams = 0
maxTopics = 0

for i in range(n - 1):
    topic_i = int(topic[i], 2)
    for j in range(i + 1, n):
        if j != i:
            topic_j = int(topic[j], 2)
            topic_i_or_j = topic_i | topic_j
            numTopics = "{0:b}".format(topic_i_or_j).count('1')

            if numTopics > maxTopics:
                maxTopics = numTopics
                numTeams = 1
            elif numTopics == maxTopics:
                numTeams += 1
                
print(maxTopics)
print(numTeams)