#Your task is to complete this function
#Function should return integer denoting the index
# indexing is done according to 0
# Left=0 and High=0
import timeit
def bin_search(arr, left, high, key):
    #Code here
    if(left <= high):
        m = (left+high)/2
        if (key == arr[m]):
            return m
        elif(key < arr[m]):
            return bin_search(arr,left,m-1,key)
        elif(key > arr[m]):
            return bin_search(arr,m+1,high,key)
    return "-1"
#x = timeit.default_timer()
t = int(raw_input())
for j in range(t):
    n = int(raw_input())
    a = map(int, raw_input().strip().split())
    k = int(raw_input())
    y = timeit.default_timer()
    x = bin_search(a,0,n-1,k)
    w = timeit.default_timer()
    print x
    print w-y
#w = timeit.default_timer()
print w-y
