import sys
input = sys.stdin.readline

n = int(input())
near_list = [[] for _ in range(n)]
par_list = list(map(int,input().split()))
root =None
for i in range(n):
    if par_list[i] !=-1:
        near_list[i].append(par_list[i])
        near_list[par_list[i]].append(i)
    else:
        root = i
r_num = int(input())

result = 0
visited = [False] * (n)

def DFS(x):
    global result
    visited[x] = True
    c_node = 0
    for i in near_list[x]:
        if not visited[i] and i != r_num:
            c_node+=1
            DFS(i)
    if c_node == 0:
        result += 1


if r_num == root:
    print(0)
else:
    DFS(root)
    print(result)


