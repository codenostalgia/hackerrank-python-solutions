#!/bin/python3

import math
import os
import random
import re
import sys

# https://www.hackerrank.com/challenges/capitalize/problem


# Complete the solve function below.
def solve(s):

    names = s.split()
    result = ""

    for name in names:
        initial = name[0]
        initial_unicode = ord(initial)
        if 97 <= initial_unicode <= 122:
            initial_unicode -= 32
            result += chr(initial_unicode)+name[1:]
        else:
            result += name
        result += " "

    result = result.strip()

    if len(s) != len(result):

        final_result = ""
        extra_spaces = 0

        for i, lett in enumerate(s):
            if not (lett == result[i-extra_spaces]) and not (abs(ord(lett)-ord(result[i-extra_spaces])) == 32):
                extra_spaces += 1
                final_result += ' '
            else:
                final_result += result[i-extra_spaces]
        return final_result

    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
