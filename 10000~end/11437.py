import sys
from collections import deque
input = sys.stdin.readline
print = sys.stdout.write
0
n = int(input())
node = [[] for _ in range(n+1)]

for _ in range(1,n):
    a, b = map(int,input().split())
    node[a].append(b)
    node[b].append(a)

parents = [0] * (n+1)
visited= [False] * (n+1)
depth = [0] * (n+1)


queue = deque()
queue.append(1)
visited[1] =True
level = 1
now_size = 1
count = 0
while queue:
    now = queue.popleft()
    for next in node[now]:
        if not visited[next]:
            visited[next] = True
            queue.append(next)
            parents[next]= now
            depth[next] = level
    count +=1
    if count == now_size:
        count = 0
        now_size = len(queue)
        level+=1


def LCA(a,b):
    if depth[a]<depth[b]:
        a,b= b,a
    while depth[a] != depth[b]:
        a= parents[a]
    while a!= b:
        a= parents[a]
        b= parents[b]
    return a

m = int(input())

for _ in range(m):
    a, b  = map(int,input().split())
    print(str(LCA(a,b)))
    print("\n")
