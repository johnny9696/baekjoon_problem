import sys
from collections import deque
input = sys.stdin.readline

# direction = ['S','W','N','E']
N= int(input())
move = input()
min_x = 0
max_x = 0
max_y = 0
min_y = 0
nd = 0
nx = 0
ny = 0
q = deque()
q.append((0,0))
for data in move:
    if data == 'R':
        nd = (nd+1)%4
    elif data == 'L':
        nd = (nd+3)%4
    elif data=='F':
        if nd == 0:
            ny +=1
            max_y = max(max_y,ny)
            q.append((nx,ny))
        elif nd == 1:
            nx -=1
            min_x = min(min_x,nx)
            q.append((nx, ny))
        elif nd == 2:
            ny -=1
            min_y = min(min_y,ny)
            q.append((nx,ny))
        else:
            nx +=1
            max_x = max(max_x,nx)
            q.append((nx,ny))
sizex = max_x - min_x
sizey = max_y - min_y
maze=[['#']*(sizex+1) for _ in range(sizey+1)]
while q:
    nx,ny = q.popleft()
    nx = nx - min_x
    ny = ny - min_y
    maze[ny][nx] = '.'
for i in range(sizey+1):
    for j in range(sizex+1):
        print(maze[i][j],end='')
    print()

