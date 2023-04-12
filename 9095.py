import sys
input = sys.stdin.readline
test = int(input())
n_list = []
for _ in range(test):
    n_list.append(int(input()))
tmp = max(n_list)
result_list = [0] * (tmp+1)
result_list[1] = 1
result_list[2] = 2
result_list[3] = 4
for i in range(4, tmp+1):
    result_list[i] = result_list[i-3]+result_list[i-2] + result_list[i-1]
for i in n_list:
    print(result_list[i])