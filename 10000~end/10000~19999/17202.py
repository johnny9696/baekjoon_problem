"""
8자씩 두번
"""
import sys
input = sys.stdin.readline
a_num = list(input())

b_num = list(input())
tmp = []
for i in range(8):
    tmp.append(int(a_num[i]))
    tmp.append(int(b_num[i]))

while len(tmp)>2:
    for i in range(len(tmp)-1):
        tmp[i] = (tmp[i] + tmp[i+1])%10
    tmp.pop()
print(str(tmp[0])+str(tmp[1]))