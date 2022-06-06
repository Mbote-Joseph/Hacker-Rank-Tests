#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    diagonal1=0
    diagonal2=0
    for i in range(len(arr)):
        for j in range(len(arr)):
            
            if( i == j):
                diagonal1 +=arr[i][j]
            if (i == len(arr)-j-1):
                diagonal2 += arr[i][j]
            
    
    return abs(diagonal1-diagonal2)
    #return abs((arr[0][0]+arr[1][1]+arr[2][2])-(arr[0][2])+arr[1]#[1]+arr[2][0])

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
