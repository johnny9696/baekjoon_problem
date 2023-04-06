import sys
from queue import PriorityQueue
input = sys.stdin.readline

V, E = map(int,input().split())
k = int(input())

near_list=[[] for _ in range(V+1)]
#간선
for i in range(E):
    u,v,w = map(int,input().split())
    near_list[u].append([v,w])

#거리 리스트
dist = [sys.maxsize] *(V+1)
visited=[False] * (V+1)


queue = PriorityQueue()
queue.put((0,k))
dist[k] = 0
while queue.qsize()>0:
    (now_dist, now) = queue.get()
    visited[now]=True
    next = near_list[now]
    for i in next:
        next, next_dist = i[0],i[1]
        if dist[next] > now_dist + next_dist:
            dist[next] = now_dist + next_dist
            queue.put((dist[next],next))

for i in range(1, V+1):
    if visited[i]:
        print(dist[i])
    else:
        print('INF')