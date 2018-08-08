"""
Convert 12 Hr Time into 24 Hr format.
"""
import os
import sys
from time import strptime, strftime

def timeConversion(s):
    return strftime("%H:%M:%S", strptime(s, "%I:%M:%S%p"))

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()
    result = timeConversion(s)
    f.write(result + '\n')
    f.close()
