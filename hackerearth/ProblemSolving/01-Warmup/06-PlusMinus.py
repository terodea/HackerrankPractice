"""
Given an array of integers, calculate the fractions of its elements that are positive, negative, and are zeros.
Print the decimal value of each fraction on a new line.
"""
import math
import os
import random
import re
import sys

def plusMinus(arr):
    positive = sum(x > 0 for x in arr) / len(arr)
    negative = sum(x < 0 for x in arr) / len(arr)
    zero = sum(x == 0 for x in arr) / len(arr)
    print(positive, negative, zero, sep="\n")

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    plusMinus(arr)
