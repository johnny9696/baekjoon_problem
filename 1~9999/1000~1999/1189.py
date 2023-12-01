import sys
from collections import deque

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

r,c,k =map(int,input().split())

maze =  [list(input()) for _ in range(r)]
visited = [[0 for _ in range(c)] for i in range(r)]
l_count = [ 0 for i in range(k+1)]

sp = (r-1, 0)
ep = (0, c-1)

def DFS(np,count):
    if count > k:
        return
    if np == ep:
        l_count[count] += 1
        return
    move = ((-1,0),(0,-1),(1,0),(0,1))

    for mx, my in move:
        next_x , next_y = np[0]+mx, np[1] + my
        if 0<= next_x <r and 0<= next_y <c:
            if not visited[next_x][next_y] and maze[next_x][next_y] != 'T':
                visited[next_x][next_y] = 1
                DFS((next_x,next_y),count + 1)
                visited[next_x][next_y] = 0
visited[sp[0]][sp[1]] = 1
DFS(sp, 1)
print(l_count[k])