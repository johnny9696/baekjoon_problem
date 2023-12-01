import sys
from collections import deque

input = sys.stdin.readline

n,m = map(int,input().split())

maze = [list(map(int,input().split())) for _ in range(n)]
dist = [[-1 for _ in range(m)] for i in range(n)]
#0 cn move 1 move 2 goal point
dq = deque()
for i in range(n):
    for j in range(m):
        if maze[i][j] == 2:
            dist[i][j] = 0
            dq.append((i,j))
        elif maze[i][j] == 0 :
            dist[i][j] = 0
move = ((-1,0),(1,0),(0,-1),(0,1))
while dq:
    now_x, now_y = dq.popleft()
    for mx,my in move:
        next_x ,next_y = now_x + mx, now_y + my
        if 0<= next_x <n and 0<= next_y <m:
            if maze[next_x][next_y] == 1:
                if dist[next_x][next_y] == -1 or dist[next_x][next_y] > dist[now_x][now_y] + 1:
                    dist[next_x][next_y] = dist[now_x][now_y] + 1
                    dq.append((next_x,next_y))

for i in range(n):
    for j in range(m):
        print(dist[i][j],end=' ')
    print()