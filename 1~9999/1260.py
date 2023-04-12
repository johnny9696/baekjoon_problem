def DFS(v):
    global visited
    global linked_list
    if 0 not in visited:
        return [v]
    result = [v]
    for i in linked_list[v]:
        if not visited[i]:
            visited[i] = 1
            result += DFS(i)
    return result


def BFS(v):
    global visited
    global linked_list
    result = [v]
    t_list =[v]
    while t_list:
        num  = t_list.pop(0)
        for i in linked_list[num]:
            if not visited[i]:
                visited[i] = 1
                t_list.append(i)
                result.append(i)
    return result



n,m,v = map(int,input().split())
linked_list= [[] for _ in range(n+1)]
for i in range(m):
    x,y = map(int,input().split())
    linked_list[x].append(y)
    linked_list[x].sort()
    linked_list[y].append(x)
    linked_list[y].sort()

visited= [0 for _ in range(n+1)]
visited[0] = 1
visited[v] = 1
result = DFS(v)
for i in result:
    print(i, end=' ')
print('')
visited= [0 for _ in range(n+1)]
visited[0] = 1
visited[v] = 1
result = BFS(v)
for i in result:
    print(i, end=' ')
