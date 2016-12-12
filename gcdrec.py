a = int(input())
b = int(input())
def gcdrec(a,b):
    if(b == 0):
        return a
    else:
        return gcdrec(b,a%b)
print gcdrec(a,b)
