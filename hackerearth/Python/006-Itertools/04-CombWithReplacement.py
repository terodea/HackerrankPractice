"""
"""
from itertools import *
s,k = input().split(' ')
for c in combinations_with_replacement (sorted(s),int(k)):
    print(''.join(c))
