import sys
from collections import deque
input = sys.stdin.readline
n= int(input())
building_time = [0] * (n+1)
b_list = [[] for _ in range(n+1)]
c_list = [[] for _ in range(n+1)]
c_count = [0] * (n+1)
for i in range(1, n+1):
    time_b = list(map(int,input().split()))
    building_time[i]= time_b.pop(0)
    while time_b:
        tmp = time_b.pop()
        if tmp != -1:
            c_count[i] +=1
            b_list[tmp].append(i)
            c_list[i].append(tmp)

queue = deque()
for i in range(1, n+1):
    if c_count[i] ==0:
        queue.append(i)

result = [0] * (n+1)
while queue:
    now= queue.popleft()
    tmp = b_list[now]
    for i in tmp:
        c_count[i] -=1
        if c_count[i] == 0:
            queue.append(i)
    max_val = 0
    tmp = c_list[now]
    for i in tmp:
        if result[i]>max_val:
            max_val = result[i]
    result[now] = building_time[now] + max_val

for i in range(1, n+1):
    print(result[i])

