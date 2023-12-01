import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n,m,r = map(int,input().split())

tree = [[] for _ in range(n+1)]
visited=[0 for _ in range(n+1)]

for _ in range(m):
    a,b = map(int,input().split())
    tree[a].append(b)
    tree[b].append(a)

def DFS(now,cnt):
    tree[now].sort()
    for i in tree[now]:
        if visited[i] == 0:
            cnt += 1
            visited[i] = cnt
            cnt = DFS(i,cnt)
    return cnt

visited[r] = 1
DFS(r,1)

for i in range(1,n+1):
    print(visited[i])