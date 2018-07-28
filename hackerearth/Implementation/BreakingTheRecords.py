"""
"""
import math
import os
import random
import re
import sys

def breakingRecords(scores):
    hb, lb = 0, -1
    a = scores[0]
    for b in scores:
        if (b>a):
            a = b
            hb +=1
    for c in scores:
        if (c<=a):
            a = c
            lb +=1
    return (hb,lb)
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    scores = list(map(int, input().rstrip().split()))
    result = breakingRecords(scores)
    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')
    fptr.close()
