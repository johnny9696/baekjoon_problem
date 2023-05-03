import sys
input = sys.stdin.readline

T = int(input())
p_list = [list(map(int,input().split())) for _ in range(T)]
result = 0
for i in range(0,T-2):
    for j in range(i+1, T-1):
        for k in range(j+1,T):
            triangle = [0,0,0]
            triangle[0] = (p_list[i][0] - p_list[j][0]) ** 2 + (p_list[i][1] - p_list[j][1]) ** 2
            triangle[1] = (p_list[i][0] - p_list[k][0]) ** 2 + (p_list[i][1] - p_list[k][1]) ** 2
            triangle[2] = (p_list[k][0] - p_list[j][0]) ** 2 + (p_list[k][1] - p_list[j][1]) ** 2
            triangle.sort()
            if triangle[2] == triangle[0] + triangle[1]:
                result+=1
print(result)