import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
n = int(input())


paper = [list(map(int,input().split())) for _ in range(n)]
bp = 0
wp = 0

def DFS(sx,sy,ex,ey):
    global bp
    global wp
    if ex==sx and ey==sy :
        if paper[sx][sy] == 0:
            wp += 1
        else:
            bp += 1
        return

    sc = paper[sx][sy]
    check = True
    for i in range(sx,ex):
        for j in range(sy,ey):
            if sc != paper[i][j]:
                check = False
                break
    if check:
        if sc:
            bp +=1
        else:
            wp +=1
    else:
        lx = (ex-sx)//2
        ly = (ey-sy)//2
        DFS(sx,sy,sx+lx,sy+ly)
        DFS(sx+lx, sy, ex, sy+ly)
        DFS(sx, sy+ly, sx+lx, ey)
        DFS(sx+lx, sy+ly, ex, ey)
    return

DFS(0,0,n,n)
print(wp)
print(bp)
