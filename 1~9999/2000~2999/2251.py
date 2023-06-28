import sys
sys.setrecursionlimit(10**6)
a,b,c = map(int,input().split())
water_now = [0,0,c]

visited=[]
result = []

def DFS(water):
    if water in visited:
        return
    else:
        visited.append(water)
    if water[0] == 0 and water[2] not in result:
        result.append(water[2])
    #a2b
    if water[0] != 0 and water[1] != b:
        t = b-water[1]
        if water[0]>t:
            DFS([water[0]-t,b,water[2]])
        else:
            DFS([0,water[0]+water[1],water[2]])
    #a2c
    if water[0] != 0 and water[2] != c:
        t = c- water[2]
        if water[0]>t:
            DFS([water[0]-t,water[1],c])
        else:
            DFS([0,water[1],water[0]+water[2]])
    #b2a
    if water[1] != 0 and water[0] !=a:
        t = a - water[0]
        if water[1]>t:
            DFS([a, water[1]-t, water[2]])
        else:
            DFS([water[0]+water[1],0,water[2]])
    #b2c
    if water[1] != 0 and water[2] !=c:
        t = c- water[2]
        if water[1]>t:
            DFS([water[0], water[1]-t, c])
        else:
            DFS([water[0], 0, water[2]+water[1]])
    #c2a
    if water[2] != 0 and water[0] != a:
        t = a- water[0]
        if water[2]>t:
            DFS([a, water[1], water[2]-t])
        else:
            DFS([water[0]+water[2], water[1], 0])
    #c2b
    if water[2] != 0 and water[1] != b:
        t = b- water[1]
        if water[2]>t:
            DFS([water[0], b, water[2]-t])
        else:
            DFS([water[0]+water[2],water[1],0])

DFS(water_now)
result.sort()
for i in result:
    print(i, end=' ')