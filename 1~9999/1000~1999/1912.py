import sys

input = sys.stdin.readline
length = int(input())
n_list = list(map(int,input().split()))

for i in range(1,len(n_list)):
    n_list[i] = max(n_list[i], n_list[i-1] + n_list[i])
print(max(n_list))