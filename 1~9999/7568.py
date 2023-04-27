import sys
input = sys.stdin.readline

n = int(input())
n_list = [list(map(int,input().split())) for _ in range(n)]

for i in range(n):
    result = 1
    for j in n_list:
        if n_list[i][0]<j[0] and n_list[i][1]<j[1]:
            result+=1
    print(result,end=' ')
