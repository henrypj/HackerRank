#!/bin/python3

import sys

# Brie’s Drawing teacher asks her class to open their n-page book to page 
# number p. Brie can either start turning pages from the front of the book 
# (i.e., page number 1) or from the back of the book (i.e., page number n), 
# and she always turns pages one-by-one (as opposed to skipping through 
# multiple pages at once). When she opens the book, page 1 is always on 
# the right side:
# 
# Each page in the book has two sides, front and back, except for the last 
# page which may only have a front side depending on the total number of 
# pages of the book.
#
# Given n and p, find and print the minimum number of pages Brie must turn 
# in order to arrive at page p.
# 
# Input Format
# 
# The first line contains an integer, n, denoting the number of pages in the book. 
# The second line contains an integer, p, denoting the page that Brie's 
# teacher wants her to turn to.
# 
# Output Format
# 
# Print an integer denoting the minimum number of pages Brie must turn to get to page .

def solve(n, p):
    # Complete this function
    numPagesFront = p // 2
    numPagesBack  = (n // 2) - (p // 2)

    return(min(numPagesFront, numPagesBack))    

n = int(input().strip())
p = int(input().strip())
result = solve(n, p)
print(result)

