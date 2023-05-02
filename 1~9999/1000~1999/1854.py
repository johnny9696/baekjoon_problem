#n도시수, m 도시간 도로수, k번째 최단 경로
#a번도시에서 b번 도시 로 c만큼 걸림
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
n, m, k = map(int,input().split())

near_list = [[] for _ in range(n+1)]
dist = [[] for _ in range(n+1)]

for i in range(m):
    a,b,c= map(int,input().split())
    near_list[a].append([b,c])

def DFS(now, distance):
    if len(dist[now]) >=k:
        m_value = max(dist[now])
        if distance>m_value:
            return
        else:
            dist[now].remove(m_value)
    dist[now].append(distance)
    for i in near_list[now]:
        if (distance + i[1]) not in dist[now]:
            DFS(i[0],distance+i[1])

DFS(1,0)
for i in range(1,n+1):
    try:
        dist[i].sort()
        print(dist[i][k-1])
    except:
        print('-1')