import sys
from queue import PriorityQueue
input= sys.stdin.readline
N,D = map(int,input().split())
dist = [i for i in range(D+1)]
q = PriorityQueue()
for _ in range(N):
    sp,ep,length = map(int,input().split())
    q.put((sp,ep,length))

dist[0] = 0
now = 1
while q.qsize()>0:
    sp, ep, length= q.get()
    if ep <=D:
        for i in range(now,sp+1):
            dist[i] = min(dist[i], dist[i-1]+1)
        dist[ep] = min(dist[sp] + length, dist[ep-1] + 1 , dist[ep])
        now = sp
for i in range(now, D+1):
    dist[i] = min(dist[i-1] + 1,dist[i])
print(dist[D])

