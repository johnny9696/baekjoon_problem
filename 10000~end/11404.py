import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

s_e = [[sys.maxsize for _ in range(n+1)] for _ in range(n+1)]
for i in range(n+1):
    s_e[i][i] = 0
for _ in range(m):
    a,b,c = map(int,input().split())
    if s_e[a][b]>c:
        s_e[a][b] = c

for k in range(1,n+1):
    for s in range(1+n):
        for e in range(1+n):
            s_e[s][e] = min(s_e[s][e],s_e[s][k]+s_e[k][e])

for i in range(1,n+1):
    for j in range(1,1+n):
        if s_e[i][j] != sys.maxsize:
            print(s_e[i][j], end=' ')
        else:
            print(0, end=' ')
    print()