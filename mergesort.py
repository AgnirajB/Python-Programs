def mergearr(d,l,m,r):
    a = d[l:m+1]
    b = d[m+1:r+1]
    a.sort()
    b.sort()
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
    d[l:r+1] = c

def mergesort(d,l,r):
    if (l < r):
        m = l+(r-l)/2
        mergesort(d,l,m)
        mergesort(d,m+1,r)

        mergearr(d,l,m,r)

n = int(raw_input())
s = map(int, raw_input().strip().split())
mergesort(s,0,n-1)
for i in s:
    print i,
