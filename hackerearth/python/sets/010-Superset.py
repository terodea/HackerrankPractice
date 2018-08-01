"""
"""
# we assume True for superset (unless we discover otherwise)
is_superset = True
#read input from stdin
A = set(input().split())
cases = int(input())
#Check for following sets
for x in range(cases):
    B = set(input().split())
    if(not A > B):
        is_superset = False
        break
#print result
print(is_superset)
