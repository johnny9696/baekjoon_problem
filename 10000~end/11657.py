import sys
input = sys.stdin.readline
#n city m bus
n,m = map(int,input().split())
edge = []

for _ in range(m):
    #a s_city, b e_city c time
    a,b,c = map(int,input().split())
    edge.append((a,b,c))

time_list = [sys.maxsize] *(n+1)
time_list[1] = 0

for _ in range(n-1):
    for s,e,t in edge:
        if time_list[s] != sys.maxsize and time_list[e]>time_list[s] +t:
            time_list[e] = time_list[s] + t

mcycle=False
for s,e,t in edge:
    if time_list[s] != sys.maxsize and time_list[e] > time_list[s] +t:
        mcycle=True

if not mcycle:
    for i in range(2, len(time_list)):
        if time_list[i]==sys.maxsize:
            print(-1)
        else:
            print(time_list[i])
else:
    print(-1)