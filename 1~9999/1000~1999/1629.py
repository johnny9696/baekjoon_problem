import sys
input = sys.stdin.readline
a,b,c = map(int,input().split())
remain_list = []
re = a
while re not in remain_list:
    re = a%c
    remain_list.append(re)

