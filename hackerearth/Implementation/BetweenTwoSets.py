"""
You will be given two arrays of integers and asked to determine all integers that satisfy the following two conditions:
  1. The elements of the first array are all factors of the integer being considered
  2. The integer being considered is a factor of all elements of the second array
"""
import os
import sys

def getTotalX(a, b):
    nmax,nmin,count = max(a),min(b),0
    for i in range(1,int(nmin/nmax)+1):
        if(sum((i*nmax)%n for n in a)+sum(n%(i*nmax) for n in b))==0:
            count+=1
    return count

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')
    nm = input().split()
    n = int(nm[0])
    m = int(nm[1])
    a = list(map(int, input().rstrip().split()))
    b = list(map(int, input().rstrip().split()))
    total = getTotalX(a, b)
    f.write(str(total) + '\n')
    f.close()
