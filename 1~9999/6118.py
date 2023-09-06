import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int,input().split())

n_list = [[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int,input().split())
    n_list[a].append(b)
    n_list[b].append(a)

dist = [sys.maxsize for _ in range(n+1)]
dist[0] = 0
dist[1] = 0
dp = deque()
dp.append(1)

while dp:
    now = dp.popleft()
    now_dist = dist[now]
    for i in n_list[now]:
        if dist[now] + 1 < dist[i]:
            dp.append(i)
            dist[i] = dist[now] + 1

m_dist = max(dist)
hidden = 0
cnt = 0
for i in range(n+1):
    if dist[i] == m_dist:
        cnt += 1
        if hidden == 0 :
            hidden = i
print(hidden, m_dist, cnt)