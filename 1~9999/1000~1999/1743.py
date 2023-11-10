import sys
from collections import deque
input = sys.stdin.readline

n,m,k = map(int,input().split())
trash = [[0 for _ in range(m)] for i in range(n)]
for _ in range(k):
    x,y = map(int,input().split())
    trash[x-1][y-1] = 1

visited = [[False for i in range(m)] for _ in range(n)]
move = ((-1,0),(1,0),(0,-1),(0,1))
def DFS(sp):
    dq = deque()
    dq.append(sp)
    cnt = 1
    while dq:
        nx,ny = dq.popleft()
        for mx,my in move:
            next_x, next_y = nx+mx, ny+my
            if 0<= next_x <n and 0<= next_y <m:
                if not visited[next_x][next_y] and trash[next_x][next_y] == 1:
                    cnt += 1
                    visited[next_x][next_y] = True
                    dq.append((next_x,next_y))
    return cnt
max_size = 0
for i in range(n):
    for j in range(m):
        if trash[i][j] == 1 and not visited[i][j]:
            visited[i][j] = True
            tmp = DFS((i,j))
            max_size = max(max_size, tmp)
print(max_size)