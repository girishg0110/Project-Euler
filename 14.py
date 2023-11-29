# Description: Which starting number, under one million, produces the longest Collatz sequence chain?

import math
import numpy as np

def solve(n):
    s = 0
    seq_length = {1 : 1}
    for i in range(2, n):
        x = i
        step_count = 0
        while x > 1:
            if x in seq_length:
                step_count += seq_length[x]
                break
            else:
                if x % 2 == 0:
                    x /= 2
                else:
                    x = 3*x+1
                step_count += 1
        seq_length[i] = step_count + 1
    s = max(range(2, n), key=seq_length.get)
    return s

if __name__ == "__main__":
    n = 1000000
    solution = solve(n)
    print(solution)