# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
a = map(int, raw_input().strip().split())
def large(s):
    b = s[0]
    for i in range(1,len(s)):
        if(b < s[i]):
            b = s[i]
    return b
for i in range(0,len(a)-1):
    z = a[i : len(a)]
    x=large(z)
    y=a.index(x)
    a[i],a[y] = a[y],a[i]
print a
