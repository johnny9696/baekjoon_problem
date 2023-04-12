import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
data = list(map(int,input().split()))
s_p = 0
e_p = len(data)-1
result = 0
data.sort()
s_num=data[s_p]+data[e_p]
while(i<j):
    if s_num == m:
        result += 1
        s_p += 1
        e_p += -1
        s_num = data[s_p] + data[e_p]
    elif s_num < m :
        s_p += 1
        s_num = data[s_p] + data[e_p]
    else:
        e_p += -1
        s_num = data[s_p] + data[e_p]
print(result)