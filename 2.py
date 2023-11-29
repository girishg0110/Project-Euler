# Description: By considering the terms in the Fibonacci sequence whose values do not exceed four million, 
                # find the sum of the even-valued terms.

def solve(n):
    s = 2
    fib = [1, 2]
    while fib[-1] <= n:
        next_term = fib[-1] + fib[-2]
        fib.append(next_term)
        if next_term % 2 == 0:
            s += next_term
    return s

if __name__ == "__main__":
    n = 4e6
    solution = solve(n)
    print(solution)