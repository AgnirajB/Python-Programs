# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
a,b = float(input()),float(input())
c = math.sqrt(a*a+b*b)
f = math.atan2(a,b)
print int(round(math.degrees(f)))
