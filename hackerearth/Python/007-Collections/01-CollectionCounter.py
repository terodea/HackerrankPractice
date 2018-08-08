from collections import Counter
_, stock = input(), Counter(list(map(int,input().split())))
money = 0
for size, cost in [map(int, input().split())
                      for _ in range(int(input()))]:
    if stock[size]>0:
        stock[size]-=1
        money+=cost
print(money)
