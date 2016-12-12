def pow(a,b):
    d = 1
    for i in range(b):
        d *= a
    return d
c = pow(2,5)
print c
print pow(2,3)
