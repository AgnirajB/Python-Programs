num = int(input())
arr = map(int, raw_input().strip().split())
key = int(raw_input())
for i in range(num):
    if (arr[i] == key):
        print i
        break
