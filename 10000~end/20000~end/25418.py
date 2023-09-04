import sys
from collections import deque
a, k = map(int,input().split())

n_list = [-1 for _ in range(k+1)]
n_list[a] = 0


dq = deque()
dq.append(a)

while dq :
    now = dq.popleft()
    next_l = [now + 1, now * 2]
    for i in next_l:
        if 0<= i < k+1:
            if n_list[i] == -1:
                n_list[i] = n_list[now] + 1
                dq.append(i)
            else:
                if n_list[i] > n_list[now] + 1:
                    n_list[i] = n_list[now] + 1
                    dq.append(i)
print(n_list[k])
