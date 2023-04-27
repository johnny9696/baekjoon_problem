"""
길이가 짧은거 우선
자리수 합이 작은 것 숫자만
알파벳 순 그다음 숫자순
우선 순위 큐로 집어 넣으면 될꺼 같음
"""
from queue import PriorityQueue
import sys
input = sys.stdin.readline
#(length, sum , data)
pq = PriorityQueue()
n = int(input())
for _ in range(n):
    text = input()
    t_list = list(text[:-1])
    s = 0
    for i in t_list:
        try:
            s += int(i)
        except:
            continue
    pq.put((len(t_list),s,text[:-1]))
while pq.qsize()>0:
    _,_,data = pq.get()
    print(data)
