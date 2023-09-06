from collections import deque
import sys
n, k = map(int,input().split())

n_list =[sys.maxsize for _ in range(200001)]

n_list[n] = 0

dq = deque()
dq.append(n)
while dq:
    now = dq.popleft()
    now_t = n_list[now]
    next = now * 2
    if next <= 200000:
        if now_t < n_list[next]:
            dq.append(next)
            n_list[next] = now_t
    if 1<=now <=200000:
        if now_t + 1 < n_list[now-1]:
            dq.append(now-1)
            n_list[now-1] = now_t + 1
    if 0<=now <200000:
        if now_t +1 < n_list[now+1]:
            dq.append(now+1)
            n_list[now+1] = now_t + 1

print(n_list[k])