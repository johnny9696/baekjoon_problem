def BFS(point,n,m):
    global maze
    visited =[[1,1]]
    depth = 1
    cp = None
    cp_list = [[[1, 1]]]
    while True:
        cp = cp_list.pop(0)
        #print(cp)
        nnp = []
        for j in cp:
            x=j[0]
            y=j[1]
            np = [[x-1,y],[x+1,y],[x,y-1],[x,y+1]]

            for i in np:
                if [i[0],i[1]] ==[n,m]:
                    return depth+1
                if maze[i[0]][i[1]] and [i[0],i[1]] not in visited:
                    visited.append([i[0],i[1]])
                    nnp.append([i[0],i[1]])
        cp_list.append(nnp)
        #print(visited)
        depth +=1


n,m = map(int,input().split())
maze = [[0 for _ in range(m+2)] for _ in range(n+2)]
for i in range(1,n+1):
    num = input()
    t_list = []
    for j in num:
        t_list.append(int(j))
    maze[i][1:-1]= t_list
#print(maze)
print(BFS([1,1],n,m))