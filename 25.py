# Description: What is the index of the first term in the Fibonacci sequence to contain digits?

import math
import numpy as np
from utils.ntheory import *

def solve(n):
    fib = [1, 1]
    while len(str(fib[-1])) < n:
        fib.append(fib[-1] + fib[-2])
    s = len(fib)
    return s

if __name__ == "__main__":
    n = 1000
    solution = solve(n)
    print(solution)