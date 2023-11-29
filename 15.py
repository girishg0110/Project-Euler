# Description: How many such routes are there through a 20x20 grid from the top-left to the bottom-right of a lattice?

import math
import numpy as np

def solve(n):
    # 2n choose n
    s = math.comb(2*n, n)
    return s

if __name__ == "__main__":
    n = 20
    solution = solve(n)
    print(solution)