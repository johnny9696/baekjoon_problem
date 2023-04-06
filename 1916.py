#도시 수 n
#버스 m
#a 2 b 비용 최소화
import sys
from queue import PriorityQueue
input = sys.stdin.readline
#n
n = int(input())
#m
m = int(input())
#출발 도시, 도착도시, 버스 비용
near_list = [[] for _ in range(n+1)]
for i in range(m):
    sp, ep, cost = map(int,input().split())
    near_list[sp].append([ep,cost])
#출발점 도착점
sp, ep = map(int,input().split())

q = PriorityQueue()
dist = [sys.maxsize] * (n+1)
visited=[False]*(n+1)
dist[sp]=0
q.put((0, sp))
while q.qsize()>0:
    now_dist, now = q.get()
    if not visited[now]:
        visited[now]=True
        for i in near_list[now]:
            next, next_dist = i[0], i[1]
            if dist[next] > now_dist + next_dist:
                dist[next] = now_dist + next_dist
                q.put((dist[next],next))

print(dist[ep])