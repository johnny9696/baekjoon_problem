num_map = [list(map(str,input().split())) for _ in range(5)]

n_list = []
move = ((-1,0),(1,0),(0,1),(0,-1))

def BFS(x,y,depth, tmp_result):
    if depth != 5:
        for mx, my in move:
            nx = x + mx
            ny = y + my
            if 0<= nx < 5 and 0<= ny <5:
                BFS(nx,ny,depth + 1, tmp_result + num_map[nx][ny])
    else:
        if tmp_result not in n_list:
            n_list.append(tmp_result)
            return


for i in range(5):
    for j in range(5):
        BFS(i, j, 0, num_map[i][j])
print(len(n_list))