import sys
from collections import deque
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
n,m,k,x = map(int,input().split())
visited = [-1] * (n+1)
link_list=[[]] * (n+1)
for i in range(m):
    a,b = map(int,input().split())
    if link_list[a] == []:
        link_list[a] = [b]
    else:
        link_list[a].append(b)
result =[]

def BFS(x):
    queue = deque()
    queue.append(x)
    visited[x] +=1
    while queue:
        now_node= queue.popleft()
        for i in link_list[now_node]:
            if visited[i]==-1:
                visited[i] = visited[now_node]+1
                queue.append(i)

BFS(x)

for i in range(n+1):
    if visited[i]==k:
        result.append(i)
if result:
    result.sort()
    for i in result:
        print(i)
else:
    print(-1)