# Description: Find the sum of the digits in the number 100!.

import math
import numpy as np
from utils.ntheory import *

def solve(n):
    s = sum(map(int, str(math.factorial(n))))
    return s

if __name__ == "__main__":
    n = 100
    solution = solve(n)
    print(solution)