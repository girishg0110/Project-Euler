# Description: What is the value of the first triangle number to have over five hundred divisors?

import math
import numpy as np
from utils.ntheory import *

def count_factors(n):
    pf = prime_factorize(n)
    num_factors = 1
    for _, v in pf.items():
        num_factors *= (v+1)
    return num_factors


def solve(n):
    s = 0
    i = 2
    while True:
        tri = i * (i+1) // 2
        if count_factors(tri) > n:
            return tri
        i += 1
    return -1


if __name__ == "__main__":
    n = 500
    solution = solve(n)
    print(solution)