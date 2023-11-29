# Description: What is the sum of the digits of the number 2^1000?

import math
import numpy as np
from utils.ntheory import *

def solve(n):
    s = 0
    s = sum(map(int, str(2**n)))
    return s

if __name__ == "__main__":
    n = 1000
    solution = solve(n)
    print(solution)