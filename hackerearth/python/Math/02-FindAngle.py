"""
"""
import math
ab = int(raw_input())
bc = int(raw_input())

hypc = math.sqrt((ab**2)+(bc**2))
acos = ((bc*bc) + (hypc*hypc) - (ab*ab)) / (2*(bc*hypc))
ans = math.degrees(math.acos(acos))

print str(int((round(ans)))) + '°'
