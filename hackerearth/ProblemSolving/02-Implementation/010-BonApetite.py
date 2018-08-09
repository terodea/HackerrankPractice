"""
https://www.hackerrank.com/challenges/bon-appetit/problem
"""
import math
import os
import random
import re
import sys

def bonAppetit(c,n,k,b):
    print('Bon Appetit' if (sum(c) - c[k]) // 2 == b else c[k] // 2)

if __name__ == '__main__':
    n, k = map(int, input().strip().split(' '))
    c = [int(x) for x in input().strip().split(' ')]
    b = int(input().strip())
    bonAppetit(c,n,k,b)
