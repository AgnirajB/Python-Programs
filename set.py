# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
s = map(float, raw_input().strip().split())
a = set(s)
print a
d = 0.0
for i in range(len(a)):
    d += a[i]
avg = d/len(a)
print avg
