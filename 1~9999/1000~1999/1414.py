"""
n개의 방
각 방에는 한개의 컴퓨터가 있음
한번이라도 연결이 되어 있으면 서로 통신이 가능함
랜선 길이의 최댓값을 구하시오
첫 줄 n
i번째 줄 j 번째 문자
0 인경우 연결 랜선 없음
a~z 는 1~26, A~Z는 27~52
불가능하면 -1
"""
import sys
from queue import PriorityQueue
input = sys.stdin.readline

c_low_list = [chr(i) for i in range(97,123)]
c_upper_list = [chr(i) for i in range(65,91)]
c_list =['0'] + c_low_list + c_upper_list

#n은 컴퓨터 수
n = int(input())
q = PriorityQueue()
max_length = 0
for i in range(n):
    tmp = input()
    for j in range(n):
        tmp_num = c_list.index(tmp[j])
        max_length += tmp_num
        if i != j and tmp_num != 0 :
            q.put((tmp_num,i,j))

parents = [i for i in range(n)]

def find(x):
    if parents[x] == x:
        return x
    else:
        parents[x] = find(parents[x])
        return parents[x]

def union(a,b):
    a = find(a)
    b = find(b)
    if a!= b:
        parents[a] = b

count = 0
while q.qsize()>0:
    v,s,e = q.get()
    if find(s) != find(e):
        union(s,e)
        max_length -= v
        count +=1

if count == n-1:
    print(max_length)
else:
    print(-1)