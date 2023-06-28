import sys
input = sys.stdin.readline
n,m,k= map(int,input().split())
f= n+m
dp_list = [[0 for _ in range(f+1)] for _ in range(f+1)]

for i in range(0, f+1):
    for j in range(0, i+1):
        if j == 0 or i == j:
            dp_list[i][j] = 1
        else:
            dp_list[i][j] = dp_list[i-1][j] + dp_list[i-1][j-1]
if dp_list[f][n]<k:
    print(-1)
else:
    result = ''
    while not (n == 0 and m == 0):
        if dp_list[n+m-1][m] >= k:
            result += 'a'
            n -= 1
        else:
            k -= dp_list[n + m - 1][m]
            result += 'z'
            m -= 1
    print(result)