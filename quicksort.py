def partition(a,l,h):
    p = a[h]
    i = -1
    for j in range(h+1):
        if (a[j] <= p):
            i += 1
            a[i],a[j] = a[j],a[i]
    return i

def quicksort(a,l,h):
     if(l < h):
         pi = partition(a,l,h)

         quicksort(a,l,pi-1)
         quicksort(a,pi+1,h)

n = int(raw_input())
a = map(int, raw_input().strip().split())
quicksort(a,0,n-1)
for i in a:
    print i,
