import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n,m = map(int,input().split())

ANT = [list(map(int,input().split())) for i in range(n)]

move = ((-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1))

result = 0
def DFS(x,y):
    ANT[x][y] = 0
    for mx,my in move:
        next_x = x + mx
        next_y = y + my
        if 0<=next_x<n and 0<=next_y<m:
            if ANT[next_x][next_y] == 1:
                DFS(next_x, next_y)

for i in range(n):
    for j in range(m):
        if ANT[i][j] == 1:
            DFS(i,j)
            result+=1

print(result)