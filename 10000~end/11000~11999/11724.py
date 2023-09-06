import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline
def search(c_num):
    global visited
    global linked
    visited[c_num] = True
    while linked[c_num]:
        t = linked[c_num].pop()
        if not visited[t]:
            search(t)


n,m= map(int,input().split())
visited = [False for _ in range(n+1)]
linked = [0 for _ in range(n+1)]
#make linked
for _ in range(m):
    p1, p2 = map(int, input().split())
    if linked[p1] == 0:
        linked[p1] = [p2]
    else:
        linked[p1].append(p2)
    if linked[p2] == 0 :
        linked[p2] = [p1]
    else:
        linked[p2].append(p1)

result = 0
for i in range(1,n+1):
    if not visited[i]:
        search(i)
        result +=1
print(result)