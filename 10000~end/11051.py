import sys
input = sys.stdin.readline
div_num = 10007
n,k = map(int,input().split())

dp_list = [[0 for _ in range(n+1)] for _ in range(n+1)]
for i in range(0, n+1):
    dp_list[i][1] = i
    dp_list[i][0] = 1
    dp_list[i][i] = 1
for i in range(2,n+1):
    for j in range(1,i):
        dp_list[i][j] = (dp_list[i-1][j]+ dp_list[i-1][j-1])%div_num
print(dp_list[n][k])