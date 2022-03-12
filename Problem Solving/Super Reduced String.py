import math
import os
import random
import re
import sys

#
# Complete the 'superReducedString' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def superReducedString(s):
    # Write your code here
    a=[]
    for i in range(len(s)):
        if len(a)==0 or a[-1]!=s[i]:
            a.append(s[i])
        else:
            a.pop()
    if len(a)==0:
        return "Empty String"
    else:
        return "".join(a)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = superReducedString(s)

    fptr.write(result + '\n')

    fptr.close()
