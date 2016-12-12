def secsort(b,n):
    for i in range(n):
        x = b.index(min(b[i:]))
        b[x],b[i] = b[i],b[x]
        print b[i],
    print ''

num = int(input())
arr = map(int, raw_input().strip().split())
secsort(arr,num)
