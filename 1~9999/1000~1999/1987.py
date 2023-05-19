import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
R,C = map(int,input().split())
world_map = [list(map(lambda x : ord(x)-65,input().rstrip())) for _ in range(R)]
visited = [False] * 26

move = [(-1,0),(1,0),(0,-1),(0,1)]
def DFS(nowx,nowy):
    result = 1
    tmp = 0
    for x_move, y_move in move:
        nextx = nowx + x_move
        nexty = nowy + y_move
        if 0<=nextx<R and 0<=nexty<C:
            next_alpha = world_map[nextx][nexty]
            if not visited[next_alpha]:
                visited[next_alpha] = True
                tmp = max(tmp,DFS(nextx,nexty))
                visited[next_alpha] = False
    return result + tmp


visited[world_map[0][0]] = True
print(DFS(0,0))