import sys
from collections import deque

input = sys.stdin.readline


m_size = int(input())

maze = [list(input()) for _ in range(m_size)]
apt = []
visited = [[0 for _ in range(m_size)] for i in range(m_size)]

def BFS(x,y):
    move = ((-1,0),(0,-1),(1,0),(0,1))
    n_count = 0
    dq = deque()
    dq.append((x,y))
    visited[x][y] = 1
    while dq :
        n_count += 1
        nx,ny = dq.popleft()
        for mx,my in move:
            next_x = nx + mx
            next_y = ny + my
            if 0<= next_x < m_size and 0<= next_y < m_size:
                if maze[next_x][next_y] == '1' and not visited[next_x][next_y]:
                    visited[next_x][next_y] = 1
                    dq.append((next_x,next_y))
    return n_count

for i in range(0,m_size):
    for j in range(0,m_size):
        if maze[i][j] == '1' and visited[i][j] == 0:
            apt.append(BFS(i,j))
print(len(apt))
apt.sort()
for i in apt:
    print(i)