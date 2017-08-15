#!/bin/python3

import sys
"""
# Description
# Difficulty: Easy
# 
# Lisa just got a new math workbook. A workbook contains exercise problems, 
# grouped into chapters.
#
# - There are n chapters in Lisa's workbook, numbered from 1 to n.
# - The i-th chapter has t(i) problems, numbered from 1 to t(i).
# - Each page can hold up to k problems. There are no empty pages or unnecessary
#   spaces, so only the last page of a chapter may contain fewer than k problems.
# - Each new chapter starts on a new page, so a page will never contain problems
#   from more than one chapter.
# - The page number indexing starts at 1.
#
# Lisa believes a problem to be special if its index (within a chapter) is the
# same as the page number where it's located. Given the details for Lisa's 
# workbook, can you count its number of special problems?
# 
# Input Format
#
# The first line contains two integers n and k — the number of chapters and the
# maximum number of problems per page respectively. 
# The second line contains n integers t(1),t(2),...,t(n), where t(i) denotes the
# number of problems in the i-th chapter.
#
# Constraints
#
# 1 <= n,k,t(i) <= 100
#
# Output Format 
#
# Print the number of special problems in Lisa's workbook.
#
# Example
#
# Given Input:
# 5 3
# 4 2 6 1 10
#
# Output:
# 4
#
# Explanation:
# The diagram below depicts Lisa's workbook with n=5 chapters and a maximum of
# k=3 problems per page. Special problems are surrounded in brackets [], and 
# page numbers are in surrounded in parenthesis ().
#
# +----------+  +----------+  +----------+  +----------+  +----------+
# |Chapter 1 |  |Chapter 1 |  |Chapter 2 |  |Chapter 3 |  |Chapter 3 |
# |          |  |          |  |          |  |          |  |          |
# | [1]      |  | 4        |  | 1        |  | 1        |  | 4        |
# |     2    |  |          |  |   2      |  |   2      |  |   [5]    |
# |       3  |  |          |  |          |  |     3    |  |       6  |
# |          |  |          |  |          |  |          |  |          |
# |(1)       |  |(2)       |  |(3)       |  |(4)       |  |(5)       |
# +----------+  +----------+  +----------+  +----------+  +----------+
#
# +----------+  +----------+  +----------+  +----------+  +----------+
# |Chapter 4 |  |Chapter 5 |  |Chapter 5 |  |Chapter 5 |  |Chapter 5 |
# |          |  |          |  |          |  |          |  |          |
# | 1        |  | 1        |  | 4        |  | 7        |  | [10]     |
# |          |  |   2      |  |   5      |  |   8      |  |          |
# |          |  |     3    |  |     6    |  |     [9]  |  |          |
# |          |  |          |  |          |  |          |  |          |
# |(6)       |  |(7)       |  |(8)       |  |(9)       |  |(10)      |
# +----------+  +----------+  +----------+  +----------+  +----------+
#
# There are 4 special problems and thus we print the number 4 on a new line.
#
# Solution
# n = number of chapters
# k = number of problems per page
# 
"""
n,k = input().strip().split(' ')
n,k = [int(n),int(k)]
p = [int(p_temp) for p_temp in input().strip().split(' ')]
pageNum = 0
specialProblems = 0

for chapter in range(n):
    pageNum += 1
    pageProblems = 0
    chapterProblems = 0
    print("Chapter ==> ", chapter)
    for problem in range(p[chapter]):
        print("Page    ==> ", pageNum)
        print("Problem ==> ", problem)
        pageProblems += 1
        chapterProblems += 1
        print("pageProblems    => ", pageProblems)
        print("chapterProblems => ", chapterProblems)
        # Special Problem found, so increment count    
        if chapterProblems == pageNum:
            print("*** chapterProblems = pageNum, Special Problem")
            specialProblems += 1
        # Increaset pageNum if there are more problems in the chapter
        if pageProblems == k and chapterProblems - (problem + 1) > 0:
            print("*** More problems, increment pageNum")
            pageProblems = 0
            pageNum += 1
        elif pageProblems == k:
            print("*** pageProblems = k, setting to 0")
            pageProblems = 0

print(specialProblems)