"""
상하 좌우 대각선은 섬
1은 땅 0 은 바다
첫줄 w h
다음줄 부터 h 개의 줄 지도
BFS써서 섬 갯수 확인
"""
import sys
from collections import deque
input = sys.stdin.readline
x_move = [-1,0,1,-1,1,-1,0,1]
y_move = [-1,-1,-1,0,0,1,1,1]
while True:
    W,H = map(int,input().split())
    if W== 0 and H == 0:
        break
    world_map = [list(map(int,input().split())) for _ in range(H)]
    visited = [[False]*W for _ in range(H)]
    island_position =deque()
    for i in range(H):
        for j in range(W):
            if world_map[i][j] == 1:
                island_position.append((i,j))
    def BFS(sx,sy):
        q= deque()
        q.append((sx,sy))
        while q:
            nowx, nowy = q.popleft()
            if not visited[nowx][nowy]:
                visited[nowx][nowy] = True
                for i in range(8):
                    nextx = nowx + x_move[i]
                    nexty = nowy + y_move[i]
                    if 0<=nextx<H and 0<=nexty<W:
                        if world_map[nextx][nexty] == 1 and not visited[nextx][nexty]:
                            q.append((nextx,nexty))
        return 1
    count = 0
    while island_position:
        x, y =island_position.popleft()
        if not visited[x][y]:
            count+= BFS(x,y)
    print(count)