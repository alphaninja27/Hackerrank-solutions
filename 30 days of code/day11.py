

import math
import os
import random
import re
import sys

def ghs(m,r,c):
    s=0
    s+=m[r-1][c-1]
    s+=m[r-1][c]
    s+=m[r-1][c+1]
    s+=m[r][c]
    s+=m[r+1][c-1]
    s+=m[r+1][c]
    s+=m[r+1][c+1]
    return s

if __name__ == '__main__':

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
mhs=-63
for i in range(1,5):
    for j in range(1,5):
        chs=ghs(arr,i,j)
        if chs>mhs:
            mhs=chs
print(mhs)