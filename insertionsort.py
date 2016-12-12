def insersort(a,n):
    for i in range(1,n):
        key = a[i]
        for j in range(i-1,-1,-1):
            if (key < a[j]):
                a[j+1] = a[j]
                if (j == 0):
                    a[j] = key
            elif(key >= a[j]):
                a[j+1] = key
                break

num = int(raw_input())
arr = map(int, raw_input().strip().split())
insersort(arr,num)
for i in arr:
    print i,
