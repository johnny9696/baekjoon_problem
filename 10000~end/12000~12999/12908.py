import sys
from collections import deque
input = sys.stdin.readline

sx, sy = map(int,input().split())
ex, ey = map(int,input().split())


min_dist = abs(sx-ex) + abs(sy - ey)
result = min_dist
teleport = [(sx,sy)]
for _ in range(3):
    x1,y1, x2,y2 = map(int,input().split())
    teleport.append((x1,y1))
    teleport.append((x2,y2))
teleport.append((ex,ey))
n_dist = [[0 for _ in range(8)] for i in range(8)]

def cal_dist(sp,ep):
    return abs(sp[0] - ep[0]) + abs(sp[1] - ep[1])

for i in range(7):
    for j in range(i+1, 8):
        if i == 0:
            n_dist[i][j] = cal_dist(teleport[i],teleport[j])
            n_dist[j][i] = cal_dist(teleport[i], teleport[j])
        elif 0< i <6:
            if i % 2 == 1:
                if i + 1 == j:
                    n_dist[i][j] = 10
                    n_dist[j][i] = 10
                else:
                    tmp = cal_dist(teleport[i], teleport[j])
                    n_dist[i][j] = tmp
                    n_dist[j][i] = tmp
            else:
                tmp = cal_dist(teleport[i], teleport[j])
                n_dist[i][j] = tmp
                n_dist[j][i] = tmp
        else:
            tmp = cal_dist(teleport[i], teleport[j])
            n_dist[i][j] = tmp
            n_dist[j][i] = tmp

p_dist = [sys.maxsize for i in range(8)]
p_dist[0]= 0
dq = deque()
dq.append(0)
while dq:
    i = dq.popleft()
    for j in range(1, 8):
        if p_dist[j] > p_dist[i] + n_dist[i][j]:
            p_dist[j] = p_dist[i] + n_dist[i][j]
            dq.append(j)
print(p_dist[-1])
