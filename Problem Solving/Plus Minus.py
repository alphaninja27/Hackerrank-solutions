#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    cp = 0
    cn = 0
    cz = 0
    for i in range(len(arr)):
        if arr[i] > 0:
            cp += 1
        elif arr[i] < 0:
            cn += 1
        else:
            cz += 1
        
    a = cp/len(arr)
    b = cn/len(arr)
    c = cz/len(arr)
        
    print(format(a,".6f"))
    print(format(b,".6f"))
    print(format(c,".6f"))

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
