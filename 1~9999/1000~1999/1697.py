import sys
from collections import deque
s,e = map(int,input().split())


visit_time = [sys.maxsize for _ in range(100001)]

dq = deque()
dq.append(s)
visit_time[s] = 0
move = [-1,1]
while dq :
    now = dq.popleft()
    for m in move :
        next_p = now + m
        if 0<= next_p <=100000:
            if visit_time[next_p] > visit_time[now] + 1:
                visit_time[next_p] = visit_time[now] + 1
                if next_p != e:
                    dq.append(next_p)
    next_p = now * 2
    if 0 <= next_p <= 100000:
        if visit_time[next_p] > visit_time[now] + 1:
            visit_time[next_p] = visit_time[now] + 1
            if next_p != e:
                dq.append(next_p)

print(visit_time[e])