import sys
from collections import deque

input = sys.stdin.readline

n,m,r = map(int,input().split())
near_list = [[] for _ in range(n+1)]

for _ in range(m):
    a,b = map(int,input().split())
    near_list[a].append(b)
    near_list[b].append(a)

visited = [False for _ in range(n+1)]

bfs_depth = [-1 for _ in range(n+1)]
bfs_width = [0 for _ in range(n+1)]

dq = deque()
dq.append(r)
bfs_depth[r] = 0
bfs_width[r] = 1
visited[r] = True
width = 2
while dq:
    now = dq.popleft()
    near_list[now].sort()
    for i in near_list[now]:
        if not visited[i]:
            bfs_depth[i] = bfs_depth[now] + 1
            bfs_width[i] = width
            visited[i] = True
            width += 1
            dq.append(i)
result = 0
for i in range(1, n+1):
    result += (bfs_depth[i] * bfs_width[i])
print(result)