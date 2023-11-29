# Description: 

import math
import numpy as np

def prime_sieve(n):
    sieve = np.ones(n+1)
    f = 2
    while f < n+1:
        if sieve[f]:
            sieve[2*f::f] = 0
        f += 1
    return sieve

def solve(n):
    s = 0
    sieve = prime_sieve(n)
    print(sieve)
    s = sum([p for p in range(2, n) if sieve[p]])
    return s

if __name__ == "__main__":
    n = 2000000
    solution = solve(n)
    print(solution)