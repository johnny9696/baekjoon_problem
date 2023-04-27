import sys
input = sys.stdin.readline

l,p = map(int,input().split())
tmp = l*p
t_list = list(map(int,input().split()))
for i in t_list:
   print(i-tmp, end=' ')