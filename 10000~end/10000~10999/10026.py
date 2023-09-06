import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

grid = [list(input()) for _ in range(n)]
GRB = 0
GB = 0
visited_RGB = [[0 for _ in range(n)] for i in range(n)]
visited_GB = [[0 for _ in range(n)] for i in range(n)]
def BFS(sp, color, visited):
    dq = deque()
    dq.append(sp)
    move = ((-1,0),(1,0),(0,-1),(0,1))
    while dq :
        nx, ny = dq.popleft()
        for mx,my in move:
            next_x,next_y = nx-mx,ny-my
            if 0<= next_x < n and 0<= next_y <n:
                if grid[next_x][next_y] in color and visited[next_x][next_y] == 0:
                    visited[next_x][next_y] = 1
                    dq.append((next_x, next_y))

for i in range(n):
    for j in range(n):
        if visited_RGB[i][j] == 0:
            if grid[i][j] == 'R':
                BFS((i,j),('R'), visited_RGB)
                GRB += 1
            elif grid[i][j] == 'G':
                BFS((i, j), ('G'), visited_RGB)
                GRB += 1
            elif grid[i][j] == 'B':
                BFS((i, j), ('B'), visited_RGB)
                GRB += 1
        if visited_GB[i][j] == 0:
            if grid[i][j] == 'R' or grid[i][j] == 'G':
                BFS((i,j),('R','G'), visited_GB)
                GB +=1
            elif grid[i][j] == 'B':
                BFS((i, j), ('B'), visited_GB)
                GB += 1
print(GRB,GB)