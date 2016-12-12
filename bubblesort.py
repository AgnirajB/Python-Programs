def bubsort(a,n):
    for i in range(n-1):
        c = 0
        for j in range(n-2):
            if (a[j] > a[j+1]):
                a[j],a[j+1] = a[j+1],a[j]
                c = 1
        if (c == 0):
            break

num = int(input())
arr = map(int, raw_input().strip().split())
bubsort(arr,num)
for i in arr:
    print i,
