#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'findNumber' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER_ARRAY arr
#  2. INTEGER k
#

def findNumber(arr, k):
    # Write your code here
    n = len(arr)
    res = ''
    for i in range(n):
        if k in (arr):
            res= 'YES'
        elif k not in (arr):
            res = 'NO'
        else:
            res = 'NO'
    return res
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = []

    for _ in range(arr_count):
        arr_item = int(input().strip())
        arr.append(arr_item)

    k = int(input().strip())

    result = findNumber(arr, k)

    fptr.write(result + '\n')

    fptr.close()
