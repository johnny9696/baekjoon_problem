import sys
input = sys.stdin.readline
dw = sys.maxsize
db = sys.maxsize

n,m = map(int,input().split())
chess = [list(input()) for i in range(n)]
# 범위 설정 0~n-7 0~m-7

for sp in range(0,n-7):
    for ep in range(0,m-7):
        tmp_dw = 0 #index 합이 even
        tmp_db = 0
        for i in range(sp,sp+8):
            for j in range(ep,ep+8):
                if chess[i][j] =='W':
                    if (i+j)%2 == 0:
                        tmp_db+=1
                    else:
                        tmp_dw +=1
                else:
                    if (i+j)%2 == 1:
                        tmp_db+=1
                    else:
                        tmp_dw+=1
        dw = min(dw,tmp_dw)
        db = min(db,tmp_db)
print(min(db,dw))




