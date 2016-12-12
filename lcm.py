a = int(input())
b = int(input())
def gcd(a,b):
    if(a<b):
        while(a > 0):
            t = a
            a = b%a
            b = t
        return t
    elif(a>b):
        while(b > 0):
            t = b
            b = a%b
            a = t
        return t
    else:
        return a
    return a
x = gcd(a,b)
print x
l = (a*b)/(x)
print l
