import sys

inpnut = sys.stdin.readline

n = int(input())

if n==1:
    print(0)
elif n ==2:
    print(1)
else:
    ans = [0 for _ in range(n+1)]
    div_num = 1000000000
    ans[1] = 0
    ans[2] = 1
    for i in range(3, n+1):
        ans[i] = (i-1)*(ans[i-1]+ans[i-2])%div_num
    print(ans[-1])

