import sys
from queue import PriorityQueue as PQ

input = sys.stdin.readline
t= int(input())
pq = PQ()
for i in range(t):
    s,e= map(int,input().split())
    pq.put((e,s))
count = 0
present_e = -1
while pq.queue:
    time = pq.get()
    end , start = time[0], time[1]
    if end>=present_e and start>=present_e:
        count +=1
        present_e = end

print(count)