import math
import os
import random
import re
import sys

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def caesarCipher(s, k):
    # Write your code here
    temp = ""
    for i in s:
        if i.isupper():
            a = 'A'
            temp += chr(ord(a) + (ord(i) - ord(a) + k)%26)
        elif i.islower():
            a = 'a'
            temp += chr(ord(a) + (ord(i) - ord(a) + k)%26)
        else:
            temp += i
    return temp

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
