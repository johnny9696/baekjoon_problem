import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
world_map = [list(map(int,input().split())) for _ in range(n) ]
num_list = [0]

for i in range(n):
    for j in range(n):
        if world_map[i][j] not in num_list:
            num_list.append(world_map[i][j])

num_list.sort()
max_cnt = 0

def find(height):
    visited = [[False ]* n for _ in range(n)]
    cnt = 0
    def BFS(sp):
        move = ((-1,0),(1,0),(0,-1),(0,1))
        dq = deque()
        dq.append(sp)
        visited[sp[0]][sp[1]] = True
        while dq:
            now_x,now_y = dq.popleft()
            for mx,my in move:
                next_x, next_y = now_x + mx , now_y + my
                if 0<= next_x < n and 0<= next_y < n:
                    if not visited[next_x][next_y] and world_map[next_x][next_y] > height:
                        visited[next_x][next_y] = True
                        dq.append((next_x,next_y))
        return 1

    for i in range(n):
        for j in range(n):
            if not visited[i][j] and world_map[i][j] > height:
                cnt += BFS((i,j))
    return cnt

for height in num_list:
    max_cnt = max(find(height), max_cnt)

print(max_cnt)
