# Description: Find the largest palindrome made from the product of two 3-digit numbers.

import math
import numpy as np

def is_prod_two_n_digit(x, n):
    for f in range(10**n-1, 10**(n-1)-1, -1):
        if (x % f == 0) and (10**(n-1) <= x // f <= 10**(n)-1):
            return True
    return False

def solve(n):
    s = 0
    for s in range((10**n - 1)**2, (10**(n-1))**2, -1):
        st = str(s)
        if (st == st[::-1]) and is_prod_two_n_digit(s, n):
            return s
    return -1

if __name__ == "__main__":
    n = 4
    solution = solve(n)
    print(solution)