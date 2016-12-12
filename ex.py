a = [1,2,3,2,2,1]
b = set(a)
s = list(b)
x = 0
for i in b:
    x += (a.count(i))/2
print x
