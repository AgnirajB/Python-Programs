# Enter your code here. Read input from STDIN. Print output to STDOUT
n,s = map(int,raw_input().strip().split())
a = []
for i in range(s):
    x = map(float,raw_input().strip().split())
    print x
    a.append(x)
m = zip(*a)
print m[1]
