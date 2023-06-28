import sys
input = sys.stdin.readline

T = int(input())
p_list = [list(map(int,input().split())) for _ in range(T)]
result = 0
for i in range(0,T-2):
    for j in range(i+1, T-1):
        for k in range(j+1,T):
            a = (p_list[i][0] - p_list[j][0]) ** 2 + (p_list[i][1] - p_list[j][1]) ** 2
            b = (p_list[i][0] - p_list[k][0]) ** 2 + (p_list[i][1] - p_list[k][1]) ** 2
            c = (p_list[k][0] - p_list[j][0]) ** 2 + (p_list[k][1] - p_list[j][1]) ** 2
            if 2*max(a,b,c) == a+b+c:
                result+=1
print(result)