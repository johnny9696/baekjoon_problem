import sys
from collections import deque
input = sys.stdin.readline
n,m = map(int,input().split())
#n은 노드 수 m은 에지수
data = [[] for _ in range(n+1)]
c_list = [0]* (n+1)
c_list[0] = -1
for i in range(m):
    a, b = map(int,input().split())
    data[a].append(b)
    c_list[b]+=1

queue = deque()
for i in range(1, n+1):
    if c_list[i] == 0:
        queue.append(i)

while queue:
    now = queue.popleft()
    print(now, end =' ')
    for  i in data[now]:
        c_list[i] -=1
        if c_list[i] ==0:
            queue.append(i)
