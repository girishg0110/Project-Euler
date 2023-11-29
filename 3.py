# Description: By considering the terms in the Fibonacci sequence whose values do not exceed four million, 
                # find the sum of the even-valued terms.
import math

def solve(n):
    s = 1
    f = 2
    while n > 1:
        if n % f == 0:
            n //= f
            s = f
        else:
            f += 1
    return s

if __name__ == "__main__":
    n = 600851475143
    solution = solve(n)
    print(solution)