import sys
from queue import PriorityQueue
"""
n,m is map size
0 is ocean, 1 is land
print the least bridge length
if every land is not able to connect print -1
"""

"""
1. island count
2. find the bridge in priorityqueue lenght, s, e
3. use the find and union algorithm
"""

input = sys.stdin.readline

n, m = map(int,input().split())

world_map = []
for i in range(n):
    world_map.append(list(map(int,input().split())))

visited = [[False for i in range(m)] for _ in range(n)]

def BFS(i,j, c):
    if world_map[i][j] == 0 or visited[i][j]:
        return False
    visited[i][j] = True
    world_map[i][j] = c
    #up
    if i>=1:
        BFS(i-1,j,c)
    #down
    if i<n-1:
        BFS(i+1,j,c)
    #left
    if j>=1:
         BFS(i,j-1,c)
    #right
    if j<m-1:
        BFS(i,j+1,c)
    return True

iscount = 1
for i in range(n):
    for j in range(m):
        if BFS(i,j,iscount):
            iscount += 1


pq = PriorityQueue()
for i in range(n):
    sp, ep, count = None, None, 0
    for j in range(m):
        if world_map[i][j] == 0:
            if sp != None:
                count +=1
        else:
            if sp == None:
                sp = world_map[i][j]
            else:
                if sp!= world_map[i][j]:
                    if ep ==None:
                        ep = world_map[i][j]
                    else:
                        sp = ep
                        ep = world_map[i][j]
                        count = 0
        if sp!= None and ep!= None and count>=2:
            pq.put((count, sp, ep))
            count = 0
            sp = ep
            ep = None

for j in range(m):
    sp, ep, count = None, None, 0
    for i in range(n):
        if world_map[i][j] == 0:
            if sp != None:
                count +=1
        else:
            if sp == None:
                sp = world_map[i][j]
            else:
                if sp!= world_map[i][j]:
                    if ep ==None:
                        ep = world_map[i][j]
                    else:
                        sp = ep
                        ep = world_map[i][j]
                        count = 0
        if sp!= None and ep!= None and count>=2:
            pq.put((count, sp, ep))
            sp = ep
            count = 0
            ep = None

parents = [i for i in range(iscount)]
def find(x):
    if parents[x] ==x :
        return x
    else:
        parents[x] = find(parents[x])
        return parents[x]

def union(a,b):
    a= find(a)
    b= find(b)
    parents[a]=b

length = 0
visited = [False] * iscount
visited[0] = True
while pq.qsize()>=1:
    dist, sp, ep = pq.get()
    #dist sp, ep
    if find(sp) != find(ep):
        length += dist
        union(sp,ep)
        visited[sp] = True
        visited[ep] = True

if False in visited:
    print(-1)
else:
    print(length)