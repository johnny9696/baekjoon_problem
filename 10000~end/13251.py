import sys
input = sys.stdin.readline
m = int(input())
gu_list = list(map(int,input().split()))
k = int(input())
s = sum(gu_list)

dp = [[0 for _ in range(s+1)] for _ in range(s+1)]

for i in range(s+1):
    dp[i][1] = i
    dp[i][i] = 1
    dp[i][0] = 1


for i in range(2, s+1):
    for j in range(1,i):
        dp[i][j] = dp[i-1][j] + dp[i-1][j-1]

tmp = 0
for i in gu_list:
    tmp += dp[i][k]

print(tmp/dp[s][k])