import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

move_x = [1, 0]
move_y = [0, 1]

path = [[0 for _ in range(n)] for j_ in range(n)]
path[0][0] = 1

maze = [list(map(int,input().split())) for _ in range(n)]

dq = deque()
dq.append((0,0))

while dq:
    nowx, nowy = dq.popleft()
    now_jump = maze[nowx][nowy]
    for i in range(2):
        mx,my = move_x[i]*maze[nowx][nowy], move_y[i]*maze[nowx][nowy]
        if 0 <= nowx+mx <n and 0<= nowy+my <n:
            path[nowx+mx][nowy+my] += path[nowx][nowy]
            if maze[nowx+mx][nowy+my] !=0:
                dq.append((nowx+mx,nowy+my))

for i in range(n):
    for j in range(n):
        if maze[i][j] == 0:
            print(path[i][j])
            break