import sys
from collections import deque
input = sys.stdin.readline

N,M,K = map(int,input().split())
bM = M

farm = [list(map(int,input().split())) for _ in range(N)]

move = [[-1,0],[0,-1],[1,0],[0,1]]

def BFS (sp):
    mush = 0
    dq = deque()
    dq.append(sp)
    while dq:
        x,y =dq.popleft()
        if farm[x][y] == 0:
            mush += 1
            farm[x][y] = 1
            for mx,my in move:
                nx = x + mx
                ny = y + my
                if  0 <= nx < N and 0<= ny < N:
                    if farm[nx][ny] == 0:
                        dq.append((nx,ny))
    return mush

pos_mush = []
for i in range(N):
    for j in range(N):
        if farm[i][j] == 0:
            pos_mush.append(BFS((i,j)))

while pos_mush:
    now = pos_mush.pop()
    if now % K !=0:
        M = M - (now // K + 1)
    else:
        M = M - (now // K)

if M>=0 and len(pos_mush) == 0 and bM != M:
    print('POSSIBLE')
    print(M)
else:
    print('IMPOSSIBLE')