import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int,input().split())
link_map = [[] for _ in range(n+1)]

for _ in range(m):
    a,b,c = map(int,input().split())
    link_map[a].append((b,c))
    link_map[b].append((a,c))

visited = [sys.maxsize for _ in range(n+1)]
visited[1] = 0
dq = deque()
dq.append(1)

while dq:
    now = dq.popleft()
    for next_p, dist in link_map[now]:
        if visited[next_p] > visited[now] + dist:
            visited[next_p] = visited[now] + dist
            dq.append(next_p)
print(visited[-1])