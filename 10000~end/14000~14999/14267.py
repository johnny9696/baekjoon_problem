import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int,input().split())
n_list = list(map(int,input().split()))
sangsa = [[] for _ in range(n+1)]
for i in range(n):
    if n_list[i] != -1:
        sangsa[n_list[i]].append(i+1)

compliment = [0 for _ in range(n+1)]

for _ in range(m):
    i, w = map(int,input().split())
    compliment[i] += w


dp = deque()
dp.append(1)
while dp:
    now = dp.popleft()
    for next_p in sangsa[now]:
        compliment[next_p] += compliment[now]
        dp.append(next_p)

for i in range(1, n+1):
    print(compliment[i], end=' ')