import sys

input = sys.stdin.readline

n, l = map(int,input().split())
leak = list(map(int,input().split()))
leak.sort()

start = leak[0]
count = 1

for location in leak[1:]:
    if location in range(start, start +l):
        continue
    else:
        start = location
        count += 1
print(count)