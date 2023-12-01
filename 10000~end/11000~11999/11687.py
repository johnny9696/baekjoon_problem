import sys
input = sys.stdin.readline
cnt = 0
n = int(input())
for i in range(0, 100000001, 5):
    tmp = i
    while tmp % 5 == 0 and tmp // 5 != 0:
        cnt += 1
        tmp = tmp // 5
    if cnt == n :
        print(i)
        break
    elif cnt > n:
        print(-1)
        break

