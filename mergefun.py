def mergefun(a,n,b,m):
    c = []
    while((len(a) > 0 )  & (len(b) > 0)):
        if (a[0] <= b[0]):
            x = a.pop(0)
            c.append(x)
        else:
            x = b.pop(0)
            c.append(x)
    if((len(a) == 0) & (len(b) != 0)):
        c = c+b
    elif((len(a) != 0) & (len(b) == 0)):
        c = c+a
    return c

n = int(raw_input())
a = map(int, raw_input().strip().split())
m = int(raw_input())
b = map(int, raw_input().strip().split())
h  = mergefun(a,n,b,m)
for i in h:
    print i,
