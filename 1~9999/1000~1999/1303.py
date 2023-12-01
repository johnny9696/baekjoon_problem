import sys
from collections import deque

input = sys.stdin.readline

n,m = map(int,input().split())

field = [list(input()) for _ in range(m)]

white = 0
blue = 0
move = ((-1,0),(1,0),(0,-1),(0,1))
def DFS(sp, type):
    dp = deque()
    dp.append(sp)
    cnt = 1
    while dp:
        x,y = dp.popleft()
        for mx,my in move:
            nx = x + mx
            ny = y + my
            if 0<= nx < m and 0<= ny < n:
                if field[nx][ny] == type:
                    field[nx][ny] = 'O'
                    dp.append((nx,ny))
                    cnt += 1
    return cnt*cnt

for i in range(m):
    for j in range(n):
        if field[i][j] == 'W':
            field[i][j] = 'O'
            white += DFS((i,j),'W')
        elif field[i][j] == 'B':
            field[i][j] = 'O'
            blue += DFS((i,j),'B')

print(white,blue)
