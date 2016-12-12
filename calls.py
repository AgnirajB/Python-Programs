# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(raw_input())
s=()
s = map(int,raw_input().strip().split())
print s
print map(hash, s)
