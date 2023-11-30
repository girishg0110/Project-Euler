# Description: What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?

import math
import numpy as np
from utils.ntheory import *

def solve(n):
    diag_sum = 1
    start = 1
    for i in range(1, n//2+1):
        for _ in range(4):
            start += 2*i
            diag_sum += start
    return diag_sum

if __name__ == "__main__":
    n = 1001
    solution = solve(n)
    print(solution)