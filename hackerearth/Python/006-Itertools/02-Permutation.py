"""
"""
from itertools import permutations
a, b = input().split()
for c in permutations(sorted(a), int(b)):
    print(''.join(c))
