# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
def fib(n):
    if(n == 0):
        return 0
    elif(n == 1):
        return 1
    else:
        return fib(n-1)+fib(n-2)
print n
a = fib(n)
print a
