import sys
from collections import deque

input = sys.stdin.readline
n,e = map(int,input().split())
l_list = [[] for  i in range(n+1)]

for _ in range(e):
    a,b,c = map(int,input().split())
    l_list[a].append((b,c))
    l_list[b].append((a,c))

must_visit = list(map(int,input().split()))
"""
경로를 총 5가지
a-v1 t1
a-v2 t2
v1-v2 t3
v1-b t4
v2-b t5
t1-t3-t5
t2-t3-t4
두가지 중 최소가 되는 값으로 구함
"""
def min_route(sp,ep):
    dist = [sys.maxsize] * (n + 1)
    dq = deque()
    dq.append(sp)
    dist[sp] = 0
    while dq:
        now = dq.popleft()
        for next_p, length in l_list[now]:
            if dist[next_p] > dist[now] + length:
                dist[next_p] = dist[now] + length
                if next_p != ep:
                    dq.append(next_p)
    return dist[ep]

dist_list = [min_route(1,must_visit[0]), min_route(1,must_visit[1]), min_route(must_visit[0],must_visit[1]),
             min_route(must_visit[0],n), min_route(must_visit[1],n)]
if sys.maxsize in dist_list:
    print(-1)
else:
    print(min(dist_list[0]+dist_list[2]+dist_list[4], dist_list[1]+dist_list[2]+dist_list[3]))
