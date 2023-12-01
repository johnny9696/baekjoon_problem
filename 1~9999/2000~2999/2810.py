import sys

input = sys.stdin.readline

n = int(input())
n_list = list(input())

cnt = 1
couple = 0
for i in n_list:
    if i == 'S':
        cnt += 1
    elif i =='L' and couple == 0:
        couple = 1
    elif i =='L' and couple ==1:
        couple = 0
        cnt += 1

if cnt > n:
    print(n)
else:
    print(cnt)