import sys
input  = sys.stdin.readline

c_node = int(input())
near_list= [[] for _ in range(c_node+1)]
for _ in range(c_node):
    tmp_list = list(map(int,input().split()))
    s = tmp_list[0]
    for i in range(1, len(tmp_list)-1, 2):
        near_list[s].append((tmp_list[i],tmp_list[i+1]))

visited = [False] * (c_node+1)
def DFS(x):
    result = 0
    visited[x] = True
    node = x
    for i in near_list[x]:
        if not visited[i[0]]:
            tmp_node, length = DFS(i[0])
            if result<length + i[1]:
                result = length +i[1]
                node = tmp_node
    return node, result

n, _ = DFS(1)
for i in range(c_node+1):
    visited[i] = False
_, result = DFS(n)
print(result)
