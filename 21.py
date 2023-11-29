# Description: Evaluate the sum of all the amicable numbers under 10000.

import math
import numpy as np
from utils.ntheory import *

def sum_factors(a):
    pf = prime_factorize(a)
    s = 1
    for k, v in pf.items():
        s*=(k**(v+1) - 1) // (k - 1)
    return s-a

def solve(n):
    s = 0
    sum_factor_list = {i : sum_factors(i) for i in range(2, n)}
    for i, x in sum_factor_list.items():
        if i == x:
            continue
        if (i == (sum_factor_list[x] if x in sum_factor_list else sum_factors(x))):
            s += i
    return s

if __name__ == "__main__":
    n = 10000
    solution = solve(n)
    print(solution)