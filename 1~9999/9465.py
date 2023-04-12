import sys

input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    sticker =[list(map(int,input().split())) for _ in range(2)]
    visited = [[0] * (n+1)  for _ in range(2)]
    visited[0][1] = sticker[0][0]
    visited[1][1] = sticker[1][0]

    for i in range(1,n):
        visited[0][i+1] = max(visited[1][i], visited[0][i-1], visited[1][i-1]) + sticker[0][i]
        visited[1][i+1] = max(visited[0][i], visited[1][i-1],visited[0][i-1]) + sticker[1][i]
    print(max(visited[0][-1],visited[1][-1]))