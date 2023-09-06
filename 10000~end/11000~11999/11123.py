import sys
from collections import deque

input = sys.stdin.readline
T = int(input())

for _ in range(T):
    H, W = map(int,input().split())
    world_map=[list(input()) for _ in range(H)]
    result = 0
    q = deque()
    x_move=[-1,1,0,0]
    y_move=[0,0,-1,1]
    for i in range(H):
        for j in range(W):
            if world_map[i][j] == '#':
                q.append((i,j))
                world_map[i][j] = '.'
                result += 1
                while q:
                    now_y,now_x = q.popleft()
                    for k in range(4):
                        next_y, next_x = now_y + y_move[k], now_x + x_move[k]
                        if 0<=next_y<H and 0<= next_x<W and world_map[next_y][next_x] == '#':
                                q.append((next_y,next_x))
                                world_map[next_y][next_x] = '.'
    print(result)

