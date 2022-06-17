#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    ampm = s[8:]
    hr = int(s[:2])
    if ampm == "PM":
        if hr == 12:
            return s[:8]
        else:
            hr += 12
            return str(hr) + s[2:8]
    elif hr == 12:
            return "00"+s[2:8]
    else:
        return s[:8]
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
