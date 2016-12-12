#code
T = int(raw_input())
for i in range(T):
    n = int(raw_input())
    a = map(int, raw_input().strip().split())
    g = set(a)
    b = list(g)
    c = 0
    for j in b:
        if (a.count(j) > (n/2)  ):
            print j
            c = 1
            break
    if (c == 0):
        print "NO Majority Element"
