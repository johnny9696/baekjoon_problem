import sys
from collections import deque

input = sys.stdin.readline
print = sys.stdout.write

n = int(input())
near_list = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    near_list[a].append(b)
    near_list[b].append(a)
depth_node = [[] for _ in range(n + 1)]

def BFS(x):
    visited = [False] * (n + 1)
    q = deque()
    q.append(x)
    visited[x] = True
    while q:
        now = q.popleft()
        for next in near_list[now]:
            if not visited[next]:
                visited[next]= True
                depth_node[next] = [next, now] + depth_node[now]
                q.append(next)
BFS(1)
m = int(input())
for _ in range(m):
    a, b = map(int, input().split())
    if len(depth_node[a]) > len(depth_node[b]):
        a,b= b,a
    a_parents = deque(depth_node[a])
    b_parents = deque(depth_node[b])
    while a!= b:
        if len(b_parents) >len(a_parents):
            b = b_parents.popleft()
        else:
            a = a_parents.popleft()
            b = b_parents.popleft()
    print(str(a)+"\n")