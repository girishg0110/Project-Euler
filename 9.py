# Description: There exists exactly one Pythagorean triplet for which a+b+c=1000. Find the product abc.

import math
import numpy as np

def solve(n):
    s = 0
    for a in range(1, n+1):
        asq = a**2
        for b in range(a+1, n+1):
            bsq = b**2
            c = n - a - b
            if (b < c) and (asq + bsq == c**2):
                return a*b*c

    return s

if __name__ == "__main__":
    n = 1000
    solution = solve(n)
    print(solution)