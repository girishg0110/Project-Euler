# Description: Find the value of d<1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.

import math
import numpy as np
from utils.ntheory import *

def recurring_cycle_length(k):
    # returns length of recurring cycle of 1/k in decimal
    dividend = 1
    remainders = {}
    i = 0
    while True:
        if dividend < k:
            dividend *= 10
        else:
            rem = dividend % k
            if rem == 0: 
                return 0
            elif rem in remainders:
                return i - remainders[rem]
            else:
                remainders[rem] = i
                dividend = rem * 10
            i += 1

def solve(n):
    s = 0
    s = max(range(1, n), key=recurring_cycle_length)
    return s

if __name__ == "__main__":
    n = 1000
    solution = solve(n)
    print(solution)