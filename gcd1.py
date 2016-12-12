a = int(input())
b = int(input())
def gcd(a,b):
    while(b>0):
        a,b = b,(a%b)
    return a
x = gcd(a,b)
print x
