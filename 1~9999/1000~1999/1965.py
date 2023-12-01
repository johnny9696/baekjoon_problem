import sys
input = sys.stdin.readline

n = int(input())
box_list = list(map(int,input().split()))

dp = [1] * n

for i in range(n):
    for j in range(i):
        if box_list[i] > box_list[j]:
            dp[i] = max(dp[i], dp[j] +1)
print(max(dp))