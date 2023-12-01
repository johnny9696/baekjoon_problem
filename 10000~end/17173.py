import sys

input = sys.stdin.readline

n,m = map(int,input().split())
n_list = list(map(int,input().split()))

ans = 0
for i in range(1, n+1):
    for j in n_list:
        if i % j == 0:
            ans += i
            break

print(ans)