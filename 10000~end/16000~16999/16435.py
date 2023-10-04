import sys

input = sys.stdin.readline
n, l = map(int,input().split())

n_list = list(map(int,input().split()))
n_list.sort()

for i in range(len(n_list)):
    if n_list[i] <= l:
        l += 1

print(l)