"""
시간의 위치는 12로 나눈 나머지
1시간에 움직이는 각도 30
1분에 0.5도
분침의 위치는 5로 나눈 몫
분당 분침은 6도
두수의 차이의 절대값 순으로 정렬
"""
import sys
input = sys.stdin.readline
T= int(input())
for _ in range(T):
    time_list = input()
    time_list = list(time_list[:-1].split(' '))
    r_list =[]
    for i in time_list:

        hh = i[:2]
        mm = i[3:]
        h_angle = float((int(hh)%12)*30) + 0.5*float(mm)
        m_angle = 6.0*float(mm)
        angle = abs(h_angle - m_angle)
        if angle >180.0:
            angle = 360.0 - angle
        r_list.append([angle, i])
    r_list.sort()
    print(r_list[2][1])