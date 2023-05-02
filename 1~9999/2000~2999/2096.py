import sys
input = sys.stdin.readline

n = int(input())
max_min = [[0,0] for _ in range(3)]
for _ in range(n):
    n_list = list(map(int,input().split()))
    temp = [[0, 0] for _ in range(3)]
    for i in range(3):
        now = n_list[i]
        if i == 0 :
            temp[i][0] = max(max_min[i][0], max_min[i+1][0]) + now
            temp[i][1] = min(max_min[i][1], max_min[i + 1][1]) + now
        elif i == 1:
            temp[i][0] = max(max_min[i-1][0], max_min[i][0] , max_min[i + 1][0]) + now
            temp[i][1] = min(max_min[i - 1][1], max_min[i][1], max_min[i + 1][1]) + now
        elif i == 2:
            temp[i][0] = max(max_min[i - 1][0], max_min[i][0]) + now
            temp[i][1] = min(max_min[i - 1][1], max_min[i][1]) + now
    max_min = temp

print(max(max_min[0][0],max_min[1][0],max_min[2][0]), end = " ")
print(min(max_min[0][1],max_min[1][1],max_min[2][1]))