"""
https://www.hackerrank.com/challenges/breaking-best-and-worst-records
"""
import math
import os
import random
import re
import sys

def breakingRecords(score):
    min_1,max_1 = score[0],score[0]
    min_brk,max_brk = 0,0
    for i in range(len(score)):
        if (score[i] < min_1):
            min_brk += 1
            min_1 = score[i]
        elif(score[i] > max_1):
            max_brk += 1
            max_1 = score[i]
    return(max_brk, min_brk)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    score = list(map(int, input().rstrip().split()))
    result = breakingRecords(score)
    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')
    fptr.close()
