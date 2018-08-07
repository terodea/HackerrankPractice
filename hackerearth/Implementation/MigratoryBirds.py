"""
"""
from collections import Counter
n = input()
arr = Counter(map(int, raw_input().split()))
print arr.most_common(1)[0][0]
