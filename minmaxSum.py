#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    n= len(arr)
    minimum= min(arr)
    maximum=max(arr)
    
    total=0
    for i in range(n):
        total +=arr[i]
        
    #for j in range(n):
      #  if j==0:
      #      total1=total-arr[j]
    #for j in range(n):
     #   if j==(n-1):
     #       total2=total-arr[j]
    print(str(total-maximum)+" "+str(total-minimum))
    

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
