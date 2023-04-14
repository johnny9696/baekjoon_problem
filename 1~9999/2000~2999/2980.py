"""
신호등의 길이를 알고 있음 시작은 모두 빨강 초록일때 초당 1미터 이동
N 신호등 갯수, L 도로의 길이
D 신호등 위치, R 빨간색 지속 G 초록색 지속
D가 증가하는 순서로 주어짐
현재 신호에서 다음 신호까지 가는 시간 빨간색 남은 시간 + 다음 신호까지의 거리
다음 신호 계산은 현재까지 걸린 시간 나누기 빨간색+초록색 지속 시간의 나머지 와 비교
"""
import sys
input = sys.stdin.readline
N,L  = map(int,input().split())
traffic = [[0,0,0]]
for _ in range(N):
    traffic.append(list(map(int,input().split())))
traffic.append([L,0,0])

cur_time = 0
for i in range(len(traffic)-1):
    pos, red, green = traffic[i]
    if pos == 0:
        cur_time = traffic[i+1][0]
    else:
        #check red
        move_time = traffic[i+1][0] - pos
        #wait time
        c_num = cur_time %(red+green)
        if c_num<red:
            wait_time = red - c_num
        else:
            wait_time = 0
        cur_time += (move_time+wait_time)
print(cur_time)