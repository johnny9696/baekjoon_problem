import sys
from collections import deque

input = sys.stdin.readline
n,m = map(int,input().split())
maze = []
dist = [[-1 for _ in range(m)] for i in range(n)]
dq = deque()
for i in range(n):
    tmp = list(map(int,input().split()))
    maze.append(tmp)
    if 2 in tmp:
        indx = tmp.index(2)
        dist[i][indx] = 0
        dq.append((i,indx))

move = ((-1,0),(1,0),(0,-1),(0,1))
while dq:
    nx,ny = dq.popleft()
    dist_n = dist[nx][ny]
    for mx,my in move:
        nextx = nx + mx
        nexty = ny + my
        if 0<= nextx <n and 0<= nexty <m:
            if maze[nextx][nexty] == 1:
                if dist[nextx][nexty] == -1:
                    dq.append((nextx,nexty))
                    dist[nextx][nexty] = dist_n + 1
                else:
                    if dist[nextx][nexty] > dist_n + 1:
                        dq.append((nextx,nexty))
                        dist[nextx][nexty] = dist_n + 1
            elif maze[nextx][nexty] == 0:
                dist[nextx][nexty] = 0

for i in range(n):
    for j in range(m):
        print(dist[i][j],end=' ')
    print()