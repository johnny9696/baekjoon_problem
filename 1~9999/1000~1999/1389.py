import sys
input = sys.stdin.readline

n, m = map(int,input().split())

friends_ship = [[sys.maxsize for _ in range(n+1)] for _ in range(n+1) ]

for i in range(n+1):
    friends_ship[i][i]= 0
    friends_ship[0][i] = 0
    friends_ship[i][0] = 0

for _ in range(m):
    a,b = map(int,input().split())
    friends_ship[a][b] = 1
    friends_ship[b][a] = 1

for k in range(1,n+1):
    for s in range(1,n+1):
        for e in range(1,n+1):
            if friends_ship[s][e] > friends_ship[s][k] + friends_ship[k][e]:
                friends_ship[s][e] = friends_ship[s][k]+friends_ship[k][e]

min_val = sys.maxsize
indx=None
for i in range(1, n+1):
    tmp = sum(friends_ship[i])
    if min_val>tmp:
        indx = i
        min_val = tmp

print(indx)


