# Description: What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

import math
import numpy as np
from collections import defaultdict

def prime_factorize(k):
    f = 2
    factors = defaultdict(lambda: 0)
    while k > 1:
        if k % f == 0:
            k /= f
            factors[f] += 1
        else:
            f += 1
    return factors

def solve(n):
    s = 1
    pf = [prime_factorize(x) for x in range(1, n+1)]
    lcm_factors = defaultdict(lambda: 0)
    for d in pf:
        for k, v in d.items():
            lcm_factors[k] = max(lcm_factors[k], v)
    prime_powers = [k ** v for k, v in lcm_factors.items()]
    for pp in prime_powers:
        s *= pp
    return s

if __name__ == "__main__":
    n = 20
    solution = solve(n)
    print(solution)