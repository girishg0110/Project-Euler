""" Description: 
You are given the following information, but you may prefer to do some research for yourself.

    1 Jan 1900 was a Monday.
    Thirty days has September,
    April, June and November.
    All the rest have thirty-one,
    Saving February alone,
    Which has twenty-eight, rain or shine.
    And on leap years, twenty-nine.
    A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
"""

import math
import numpy as np
from utils.ntheory import *

def month_length(month, year):
    if month == 2:
        if ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0):
            return 29
        return 28
    if month in [9,4,6,11]:
        return 30
    return 31
    
def solve(n):
    month, year, dayofweek = 1, 1900, 1
    sunday_count = 0
    while (month <= 12) and (year <= n):
        if dayofweek == 0 and (year >= 1901):
            sunday_count += 1
        dayofweek = (dayofweek + month_length(month, year)) % 7
        month += 1
        if month == 13:
            month = 1
            year += 1

    s = sunday_count
    return s

if __name__ == "__main__":
    n = 2000
    solution = solve(n)
    print(solution)