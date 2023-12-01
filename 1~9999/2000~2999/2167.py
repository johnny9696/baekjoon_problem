import sys

input = sys.stdin.readline

n,m=map(int,input().split())

n_list = [list(map(int,input().split())) for _ in range(n)]
n = int(input())

for _ in range(n):
    sx,sy,ex,ey = map(int,input().split())
    result = 0
    for i in range(sx-1,ex):
         result += sum(n_list[i][sy-1:ey])
    print(result)