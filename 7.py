# Description: What is the 10001st prime number?

import math
import numpy as np

def is_prime(k):
    for f in range(2, k):
        if k % f == 0:
            return False
    return True

def solve(n):
    s = 0
    primes = []
    k = 2
    while len(primes) < n:
        if is_prime(k):
            primes.append(k)
        k += 1
    s = primes[-1]
    return s

if __name__ == "__main__":
    n = 10001
    solution = solve(n)
    print(solution)