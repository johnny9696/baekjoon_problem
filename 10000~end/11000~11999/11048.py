import sys
input = sys.stdin.readline

n,m = map(int,input().split())
arr = [[0]*(m+1)] + [[0]+list(map(int,input().split())) for i in range(n)]
dp = [[0]*(m+1) for i in range(n+1)]
for i in range(1,n+1):
    for j in range(1,m+1):
        dp[i][j] = max(dp[i-1][j],dp[i][j-1])+arr[i][j]
print(dp[n][m])