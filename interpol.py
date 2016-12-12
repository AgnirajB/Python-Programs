def interpool(arr,low,high,key):
    if(low <= high):
        pos = low + ((key-arr[low])*(high-low)/(arr[high]-arr[low]))
        if (key == arr[pos]):
            return pos
        elif (key < arr[pos]):
            return interpool(arr,low,pos-1,key)
        elif(key > arr[pos]):
            return interpool(arr,pos+1,high,key)
    return -1

num = int(input())
arr = map(int, raw_input().strip().split())
key = int(raw_input())
h = interpool(arr,0,num-1,key)
print h
