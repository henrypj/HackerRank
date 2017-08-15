#!/bin/python3

import sys

# If year >= 1919, Gregorian calendar
#    Leap year is divisible by 400 or
#                 divisible by 4, but not 100
# If year = 1918, *** Special Case *** Feb 14 = 32nd day
# If year <= 1918, Julian calendar
#    Leap year is divisible by 4


def solve(year):
    # Complete this function
    if year <= 1917:       # Julian Calendar
        if year % 4 == 0:  # Check if leap year
            return "12.09.%s" %year
        else:
            return "13.09.%s" %year
    elif year == 1918:      # Gregorian Calendar
        return("26.09.1918")
    else:
        if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
            return "12.09.%s" %year
        else:
            return "13.09.%s" %year

year = int(input().strip())
result = solve(year)
print(result)
