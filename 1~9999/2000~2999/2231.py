import sys
input = sys.stdin.readline
n = int(input())
t = n
m_min = 1
m_max = 0
find = False
for i in range(1,n+1):
    tmp_r = i
    t = i
    while t>0:
        tmp_r += t%10
        t=t//10
    if tmp_r == n:
        find = True
        result = i
        break
if find:
    print(result)
else:
    print(0)