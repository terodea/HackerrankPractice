"""
Capitalize the First Name and Last Name's initial letter.
i/p: ram singh
o/p: Ram Singh
"""
import math
import os
import random
import re
import sys
def solve(s):
  return ' '.join(i.capitalize() for i in s.split(' '))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
