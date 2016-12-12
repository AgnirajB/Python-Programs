def rec_pow(a,b):
    if (b == 0):
        d=1
    elif(a == 1):
        d=1
    else:
        d=a*rec_pow(a,b-1)
    return d
s = rec_pow(4,4)
print s
