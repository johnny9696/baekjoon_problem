import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
n_list = list(map(int,input().split()))

visited = [sys.maxsize for _ in range(n)]

visited[0] = 0


dp = deque()
dp.append(0)
while dp :
    now = dp.popleft()
    move = n_list[now]

    for i in range(1,move+1):
        if 0<=now + i<n:
            if visited[now + i] > visited[now] + 1:
                dp.append(now + i)
                visited[now + i] = visited[now] + 1

if visited[-1] != sys.maxsize:
    print(visited[-1])
else:
    print(-1)
