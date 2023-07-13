import sys
from collections import deque

def min_chess(map_size,sp,ep):
    chess_map = [[sys.maxsize for _ in range(map_size)] for i in range(map_size)]
    dq = deque()
    dq.append(sp)
    chess_map[sp[0]][sp[1]] = 0
    move_x = [-1,1,-2,2,-2,2,-1,1]
    move_y = [-2,-2,-1,-1,1,1,2,2]
    while dq :
        now_x, now_y = dq.popleft()
        if (now_x,now_y) == ep:
            break
        n_move = chess_map[now_x][now_y]
        for i in range(8):
            if 0 <= now_x+move_x[i]<map_size and 0<= now_y + move_y[i]<map_size:
                np_x = now_x + move_x[i]
                np_y = now_y + move_y[i]
                if chess_map[np_x][np_y] > n_move + 1:
                    chess_map[np_x][np_y] = n_move + 1
                    dq.append((np_x,np_y))
    return chess_map[ep[0]][ep[1]]
Test_case = int(input())
for _ in range(Test_case):
    chess = int(input())
    sx,sy = map(int,input().split())
    ex,ey = map(int,input().split())
    print(min_chess(chess,(sx,sy),(ex,ey)))
