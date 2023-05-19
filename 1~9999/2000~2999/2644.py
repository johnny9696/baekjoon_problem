import sys
from collections import deque
input = sys.stdin.readline

N= int(input())
s, e = map(int,input().split())

p_c = [[] for _ in range(N+1)]

M = int(input())
for i in range(M):
    p,c = map(int,input().split())
    p_c[p].append(c)
    p_c[c].append(p)

visited = [sys.maxsize] * (N+1)
q= deque()
visited[s] = 0
q.append(s)
while q:
    now = q.popleft()
    for i in p_c[now]:
        if visited[now] + 1 < visited[i]:
            visited[i] = visited[now] + 1
            q.append(i)
if visited[e] != sys.maxsize:
    print(visited[e])
else:
    print(-1)