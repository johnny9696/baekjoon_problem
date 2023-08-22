import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n, m = map(int,input().split())
    country = [[] for _ in range(n+1)]
    for _ in range(m):
        a,b = map(int,input().split())
        country[a].append(b)
        country[b].append(a)