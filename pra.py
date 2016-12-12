import timeit
a = int(input())
b = int(input())
q = timeit.default_timer()

def gcd(a,b):
    while(b>0):
        a,b = b,(a%b)
    return a
x = gcd(a,b)
print x
w = timeit.default_timer()
print w-q
