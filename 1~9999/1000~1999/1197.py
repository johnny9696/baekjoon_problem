import sys
from queue import PriorityQueue
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
v,e = map(int,input().split())
pq = PriorityQueue()

for _ in range(e):
    a,b,c = map(int,input().split())
    pq.put((c,a,b))

base_node = [i for i in range(0,v+1)]

def find(x):
    if base_node[x] == x:
        return x
    else:
        base_node[x] = find(base_node[x])
        return base_node[x]

def union(a,b):
    a= find(a)
    b = find(b)
    if a!= b:
        base_node[a] = b

result = 0
used_edge = 0
while used_edge < v-1:
    (dist, node_a, node_b) = pq.get()
    if find(node_a) != find(node_b):
        union(node_a,node_b)
        result += dist
        used_edge+=1

print(result)