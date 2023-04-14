"""
시간의 위치는 12로 나눈 나머지
분침의 위치는 5로 나눈 몫
두수의 차이의 절대값 순으로 정렬

"""

import sys
input = sys.stdin.readline
T= int(input())
for _ in range(T):
    time_list = list(map(str,input().split(' ')))
    r_list =[]
    for i in time_list:
        hh = float(int(i[:2])%12)
        mm = int(i[3:])/5
        angle = abs(hh-mm)
        if angle>6:
            angle = 12.0 - angle
        r_list.append((angle, i))
    r_list.sort()
    print(r_list[2][1])