import sys
from collections import deque
input = sys.stdin.readline


a,b,s,e = map(int,input().split())

move = [-1,1,a,-a,b,-b]
jump = [a, b]
visited = [sys.maxsize for _ in range(100001)]
visited[s] = 0

dq = deque()
dq.append(s)
while dq:
    now = dq.popleft()
    for m in move:
        next_p = now + m
        if 0<=next_p<=100000:
            if visited[next_p] > visited[now] + 1:
                visited[next_p] = visited[now] + 1
                if next_p != e:
                    dq.append(next_p)
    for j in jump:
        next_p = now * j
        if 0<= next_p <= 100000:
            if visited[next_p] > visited[now] + 1:
                visited[next_p] = visited[now] + 1
                if next_p != e:
                    dq.append(next_p)
print(visited[e])
