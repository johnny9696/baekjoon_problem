import sys
from collections import deque

input =sys.stdin.readline

n,m,r = map(int,input().split())

near_list = [[] for _ in range(n+1)]

for _ in range(m):
    a,b = map(int,input().split())
    near_list[a].append(b)
    near_list[b].append(a)

visited = [-1 for _ in range(n+1)]
dq = deque()
dq.append(r)
visited[r] = 0
while dq:
    now = dq.popleft()
    for i in near_list[now]:
        if visited[i] == -1:
            visited[i] = visited[now] + 1
            dq.append(i)
for i in range(1, n+1):
    print(visited[i])