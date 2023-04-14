import sys
input = sys.stdin.readline

s_player = int(input())
ti_ta_to = [[0]*4 for _ in range(4)]

def who_wins():
    #row and col
    for i in range(1,4):
        rt = True
        ct = True
        for j in range(2,4):
            #row
            if rt and ti_ta_to[i][1] != ti_ta_to[i][j]:
                rt = False
            #col
            if ct  and ti_ta_to[1][i] != ti_ta_to[j][i]:
                ct = False
        if rt:
            return ti_ta_to[i][1]
        if ct:
            return ti_ta_to[1][i]
    #cross
    if ti_ta_to[2][2] == ti_ta_to[1][1] and ti_ta_to[2][2] == ti_ta_to[3][3]:
        return ti_ta_to[2][2]
    if ti_ta_to[2][2] == ti_ta_to[1][3] and ti_ta_to[2][2] == ti_ta_to[3][1]:
        return ti_ta_to[2][2]
    return 0

while True:
    try :
        x,y =map(int,input().split())
    except:
        break
    ti_ta_to[x][y] = s_player
    if s_player == 1:
        s_player = 2
    else:
        s_player = 1
    winner = who_wins()
    if winner != 0:
        break
print(winner)
