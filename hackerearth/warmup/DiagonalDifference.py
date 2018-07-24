"""
Given a square matrix, calculate the absolute difference between the sums of its diagonals.
"""

import math
import os
import random
import re
import sys

def diagonalDifference(arr):
    """
    One Liner Solution
    print(abs(sum((lambda arr: int(arr[x]) - int(arr[len(arr) - x - 1]))(input().split()) for x in range(int(input())))))
    """
    sum1  = 0
    sum2  = 0
    for i in range(n):
        sum1 += int(arr[i][i])
        sum2 += int(arr[i][n-i-1])
    return abs(sum1 - sum2)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)
    fptr.write(str(result) + '\n')
    fptr.close()
