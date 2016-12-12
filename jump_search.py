import math
def jpsearch(a,n,k):
    s = int(math.sqrt(n))
    j = n/s
    if(k == a[0]):
        return 0
    for i in range(1,j):
        ind = j*i
        if (k < a[ind]):
            for r in range(j):
                if(k == a[ind-r]):
                    return ind-r
    for l in range(n-j,n):
        if (k == a[l]):
            return l

num = int(input())
arr = map(int, raw_input().strip().split())
key = int(raw_input())
h = jpsearch(arr,num,key)
print h
