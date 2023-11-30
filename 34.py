# Description: Find the sum of all numbers which are equal to the sum of the factorial of their digits.

import math
import numpy as np
from utils.ntheory import *

def solve(n):
    s = 0
    factorials = [1]
    for i in range(1, 10):
        factorials.append(i * factorials[-1])
    for i in range(3, 10**6):
        if i == sum(map(lambda x: factorials[x], map(int, str(i)))):
            s += i
    return s

if __name__ == "__main__":
    n = 100
    solution = solve(n)
    print(solution)