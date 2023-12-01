import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int,input().split())

shark = [list(map(int,input().split())) for _ in range(n)]
dq = deque()
for i in range(n):
    for j in range(m):
        if shark[i][j] == 1:
            dq.append((i,j))
def BFS(dq):
    x_move = [-1,0,1,-1,1,-1,0,1]
    y_move = [-1,-1,-1,0,0,1,1,1]
    while dq:
        x_now,y_now = dq.popleft()
        now = shark[x_now][y_now]
        for i in range(8):
            x_next = x_now + x_move[i]
            y_next = y_now + y_move[i]
            if 0<=x_next<n and 0<=y_next<m:
                if shark[x_next][y_next] == 0:
                    shark[x_next][y_next] = now+1
                    dq.append((x_next,y_next))
                else:
                    if shark[x_next][y_next] > now+1:
                        shark[x_next][y_next] = now+1
                        dq.append((x_next,y_next))

BFS(dq)
result = 0
for i in range(n):
    result = max(result,max(shark[i]))
print(result-1)

