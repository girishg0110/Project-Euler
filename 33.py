# Description: If the product of these four fractions is given in its lowest common terms, find the value of the denominator.

import math
import numpy as np
from utils.ntheory import *

def solve(n):
    s = 0
    fractions = []
    for i in range(1, 10):
        for j in range(1, 10):
            if i == j:
                continue
            if (9*i*j) % (10*i-j) == 0:
                a = (9*i*j) // (10*i-j)
                if 1 <= a <= 9:
                    fractions.append((i, j))

    prod_fraction = [1, 1]
    for n, d in fractions:
        prod_fraction[0] *= n
        prod_fraction[1] *= d
    s = prod_fraction[1] // gcf(prod_fraction)
    return s

if __name__ == "__main__":
    n = 100
    solution = solve(n)
    print(solution)