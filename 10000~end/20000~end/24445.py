import sys
from collections import deque

input = sys.stdin.readline

n,m,r = map(int,input().split())

near_list =[[] for _ in range(n+1)]

for _ in range(m):
    s,e = map(int,input().split())
    near_list[s].append(e)
    near_list[e].append(s)

visited= [0 for _ in range(n+1)]
dq = deque()
dq.append(r)
i = 1
while dq:
    now = dq.popleft()
    if visited[now] == 0:
        visited[now] = i
        i+=1
        near_list[now].sort(reverse=True)
        for j in near_list[now]:
            if visited[j] == 0:
                dq.append(j)

for i in range(1, n+1):
    print(visited[i])
