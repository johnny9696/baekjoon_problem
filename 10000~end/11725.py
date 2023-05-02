import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
n = int(input())


near_list = [[] for _ in range(n+1)]
for _ in range(n-1):
    s, e = map(int,input().split())
    near_list[s].append(e)
    near_list[e].append(s)

visited = [False] * (n+1)
parents = [0] * (n+1)

def DFS(x):
    if visited[x]:
        return
    visited[x] = True
    tmp = near_list[x]
    for i in tmp:
        if not visited[i]:
            parents[i] = x
            DFS(i)

DFS(1)
for i in range(2, len(parents)):
    print(parents[i])