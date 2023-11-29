# Description: Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, 
                # begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, 
                # multiply this value by its alphabetical position in the list to obtain a name score. 
                # What is the total of all the name scores in the file?

import math
import numpy as np
from utils.ntheory import *

def get_string_val(string):
    return sum(map(lambda c: ord(c) - 64, string))

def solve(n):
    s = 0
    with open(n, "r") as file:
        names = file.read().replace('"', '').replace("'", '').split(",")
    names = sorted(names)
    for i, name in enumerate(names):
        s += get_string_val(name) * (i + 1)
    return s

if __name__ == "__main__":
    n = "0022_names.txt"
    solution = solve(n)
    print(solution)