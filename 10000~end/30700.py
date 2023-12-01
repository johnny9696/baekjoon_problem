import sys

input = sys.stdin.readline

n_list = list(input())

k_list = list('KOREA')

cnt = 0
for char in n_list:
    now = k_list[cnt%5]
    if char == now:
        cnt += 1
print(cnt)