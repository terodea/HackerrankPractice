"""
You are choreographing a circus show with various animals.
For one act, you are given two kangaroos on a number line ready to jump in the positive direction (i.e, toward positive infinity).
1.The first kangaroo starts at location 'x1' and moves at a rate of 'v1' meters per jump.
2.The second kangaroo starts at location 'x2' and moves at a rate of 'v2' meters per jump.
"""
import math
import os
import random
import re
import sys

def kangaroo(x1, v1, x2, v2):
    if((x1>x2 and v1>v2) or (x1<x2 and v1<v2) or (v1-v2)==0):
        return "NO"
    if((x1 - x2) % (v2 - v1)) == 0:
        return "YES"
    else:
        return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    x1V1X2V2 = input().split()
    x1 = int(x1V1X2V2[0])
    v1 = int(x1V1X2V2[1])
    x2 = int(x1V1X2V2[2])
    v2 = int(x1V1X2V2[3])
    result = kangaroo(x1, v1, x2, v2)
    fptr.write(result + '\n')
    fptr.close()
