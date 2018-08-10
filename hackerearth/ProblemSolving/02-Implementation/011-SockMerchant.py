"""
https://www.hackerrank.com/challenges/sock-merchant/problem
"""
import math
import os
import random
import re
import sys

def sockMerchant(n, ar):
    tot,d = 0,{}
    for i in range(n):
        if ar[i] in d:
            d.pop(ar[i])
            tot += 1
        else:
            d[ar[i]] = 1
    return tot

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    ar = list(map(int, input().rstrip().split()))
    result = sockMerchant(n, ar)
    fptr.write(str(result) + '\n')
    fptr.close()
