# Description: Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.

import math
import numpy as np
from utils.ntheory import *

def solve(n):
    s = 0
    for i in range(10, 1000000):
        if i == sum(map(lambda x: x**n, map(int, str(i)))):
            s += i
    return s

if __name__ == "__main__":
    n = 5
    solution = solve(n)
    print(solution)