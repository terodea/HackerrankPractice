"""
"""
import itertools

task = input().split()
n, denom = int(task[0]), int(task[1])

ans = [input().split()[1:] for i in range(n)]
ans = list(itertools.product(*ans))
ans = [sum([(int(x)**2) for x in l]) for l in ans]

print(max(i%denom for i in ans))
