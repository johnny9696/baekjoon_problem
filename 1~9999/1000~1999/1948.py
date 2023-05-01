import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
#정방향 역방향
p_list=[[] for _ in range(n+1)]
rp_list = [[] for _ in range(n+1)]
c_edge = int(input())
c_count = [0] * (n+1)
for i in range(c_edge):
    s,e,time = map(int, input().split())
    p_list[s].append([e,time])
    rp_list[e].append([s,time])
    c_count[e] +=1
#road count, time
r_time = [0] *(n+1)
s,e = map(int,input().split())

queue = deque()
queue.append(s)
while queue:
    tmp  = queue.popleft()
    for i in p_list[tmp]:
        c_count[i[0]] -=1
        if c_count[i[0]] == 0:
            queue.append(i[0])
            for j in rp_list[i[0]]:
                before = r_time[j[0]]
                now = r_time[i[0]]
                if before + j[1] > now:
                    r_time[i[0]] = before + j[1]

print(r_time[e])
queue.clear()
queue.append(e)
visited= [False] * (n+1)
r_count = 0
while queue:
    now = queue.popleft()
    for next in rp_list[now]:
        if r_time[next[0]] + next[1] == r_time[now]:
           r_count+=1
           if not visited[next[0]]:
               visited[next[0]] = True
               queue.append(next[0])
print(r_count)