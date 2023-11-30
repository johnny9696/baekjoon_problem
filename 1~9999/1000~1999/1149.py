import sys

input = sys.stdin.readline

n = int(input())

RGB = [list(map(int,input().split())) for _ in range(n)]
min_path = [RGB[0]]

for i in range(1,n):
    min_path.append([min(min_path[i-1][1], min_path[i-1][2]) + RGB[i][0], min(min_path[i-1][0], min_path[i-1][2]) + RGB[i][1],min(min_path[i-1][1], min_path[i-1][0]) + RGB[i][2]])

print(min(min_path[-1]))