import sys
from collections import deque

input = sys.stdin.readline

m,n = map(int,input().split())
maze = [list(input()) for _ in range(m)]

dq = deque()
for i in range(n):
    if maze[0][i] == '0':
        maze[0][i] = '2'
        dq.append((0,i))

move = ((-1, 0),(1, 0),(0, 1),(0,-1))
while dq:
    nx,ny = dq.popleft()
    for mx, my in move:
        nextx = nx + mx
        nexty = ny + my
        if 0<=nexty<n and 0<= nextx <m:
            if maze[nextx][nexty] == '0':
                maze[nextx][nexty] = '2'
                dq.append((nextx,nexty))

pos = False
for i in range(n):
    if maze[m-1][i] == '2':
        pos = True
        break
if pos:
    print('YES')
else:
    print('NO')