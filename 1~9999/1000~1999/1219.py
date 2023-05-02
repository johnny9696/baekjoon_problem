import sys
input = sys.stdin.readline

#city  sp ep  trans
n_city, sp, ep, trans = map(int,input().split())

money = [-sys.maxsize] * n_city

edge = []
for _ in range(trans):
    start, end, cost = map(int,input().split())
    edge.append((start, end, cost))

effort = list(map(int,input().split()))
money[sp]=effort[sp]
for _ in range(n_city-1):
    for start, end, cost in edge:
        if money[start] != -sys.maxsize and money[end]< money[start] + effort[end] - cost:
            money[end] = money[start] + effort[end] - cost


for _ in range(101):
    for start, end, cost in edge:
        if money[start] != -sys.maxsize and money[end] < money[start] + effort[end] - cost :
            money[end]=sys.maxsize

if money[ep]==sys.maxsize:
    print('Gee')
elif money[ep] == -sys.maxsize:
    print('gg')
else:
    print(money[ep])

