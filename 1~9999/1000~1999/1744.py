from queue import PriorityQueue
import sys
input = sys.stdin.readline
pq_plus = PriorityQueue()
pq_minus = PriorityQueue()

T = int(input())
for i in range(T):
    tmp = int(input())
    if tmp>0:
        pq_plus.put(-tmp)
    else:
        pq_minus.put(tmp)

result = 0
t2 = None
while pq_plus.qsize()>1:
    t1 = -pq_plus.get()
    t2 = -pq_plus.get()
    if t1 != 1 and t2 != 1:
        result += (t1*t2)
    else:
        result = result + t1 + t2
if pq_plus.queue:
    result += -pq_plus.get()

while pq_minus.qsize()>1:
    t1 = pq_minus.get()
    t2 = pq_minus.get()
    result += (t1*t2)

if pq_minus.queue:
    result += pq_minus.get()

print(result)