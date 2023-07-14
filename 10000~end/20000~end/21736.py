import sys
from collections import deque

sys.setrecursionlimit(10**6)


n,m = map(int,input().split())
campus = [list(input()) for _ in range(n)]
result = 0

for i in range(n):
    for j in range(m):
        if campus[i][j] == 'I':
            sx = i
            sy = j
            break

move = ((-1,0),(0,-1),(1,0),(0,1))
visited = [[False for _ in range(m)] for i in range(n)]
visited[sx][sy] = True
dq =deque()
dq.append((sx,sy))

while dq :
    nx, ny = dq.popleft()
    for mx,my in move:
        if 0<= nx+mx <n and 0<= ny+my <m:
            if not visited[nx + mx][ny + my] and campus[nx+mx][ny+my] != 'X':
                visited[nx+mx][ny+my] = True
                if campus[nx+mx][ny+my] == 'P':
                    result +=1
                dq.append((nx+mx,ny+my))


if result == 0:
    print('TT')
else:
    print(result)