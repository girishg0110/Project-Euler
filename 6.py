# Description: Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

import math
import numpy as np

def solve(n):
    s = 0
    ssq = sum(map(lambda x: x**2, range(1, 10**n+1)))
    sqs = sum(range(1, 10**n+1))**2
    s = sqs - ssq
    return s

if __name__ == "__main__":
    n = 2
    solution = solve(n)
    print(solution)