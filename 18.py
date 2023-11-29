# Description: Find the maximum total from top to bottom of the triangle below:

import math
import numpy as np
import copy
from utils.ntheory import *

def solve(n):
    # construct a identical grid storing the max value path from the top ending at that node
    grid = [list(map(int, x.split(" "))) for x in n.split("\n")]
    pathvals = [[0] * i for i in range(1, len(grid)+1)]
    queue = [(0,0)] # start at row 0, col 0
    while queue:
        row, col = queue.pop(0)
        pathvals[row][col] = max(grid[row][col], pathvals[row][col])
        if row + 1 < len(pathvals):
            pathvals[row+1][col] = max(grid[row+1][col] + pathvals[row][col], pathvals[row+1][col])
            pathvals[row+1][col+1] = max(grid[row+1][col+1] + pathvals[row][col], pathvals[row+1][col+1])
            queue.extend([(row+1, col), (row+1, col+1)])
    s = max(pathvals[-1])
    return s

if __name__ == "__main__":
    n = """75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"""
    solution = solve(n)
    print(solution)