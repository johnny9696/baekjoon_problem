import sys
from collections import deque

input = sys.stdin.readline
n,m,r = map(int,input().split())

near_list = [[] for j in range(n+1)]
visited = [0 for _ in range(n+1)]

for _ in range(m):
    s,e = map(int,input().split())
    near_list[s].append(e)
    near_list[e].append(s)

dq = deque()
dq.append(r)
j=1
while dq:
    now = dq.popleft()
    if visited[now] == 0 :
        visited[now] = j
        j += 1
        near_list[now].sort()
        for i in near_list[now]:
            if visited[i] == 0:
                dq.append(i)


for i in range(1, n+1):
    print(visited[i])