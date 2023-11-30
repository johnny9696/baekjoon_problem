import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
room = [[] for _ in range(n+1)]

for _ in range(n-1):
    a,b,c = map(int,input().split())
    room[a].append((b,c))
    room[b].append((a,c))

dist = [sys.maxsize for _ in range(n+1)]
dist[1] = 0
dq = deque()
dq.append(1)

while dq:
    now = dq.popleft()
    for r, d in room[now]:
        if dist[r] > dist[now] + d:
            dist[r] = dist[now] + d
            dq.append(r)

print(max(dist[1:]))

