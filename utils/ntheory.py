from collections import defaultdict
import numpy as np

def is_prime(k):
    for f in range(2, k):
        if k % f == 0:
            return False
    return True

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

def prime_sieve(n):
    sieve = np.ones(n+1)
    f = 2
    while f < n+1:
        if sieve[f]:
            sieve[2*f::f] = 0
        f += 1
    return sieve