import sys
input = sys.stdin.readline

n = int(input())

path = [[0 for _ in range(n+1)] for _ in range(n+1)]
for i in range(1,n+1):
    tmp=list(map(int,input().split()))
    for j in range(len(tmp)):
        path[i][j+1] = tmp[j]

for k in range(1, n+1):
    for s in range(1, n+1):
        for e in range(1, n+1):
            if path[s][k]==1 and path[k][e] ==1:
                path[s][e] = 1
for i in range(1, n+1):
    for j in range(1, n+1):
        if path[i][j] >=1 :
            print(1, end=' ')
        else:
            print(0, end=' ')
    print()