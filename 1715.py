import sys
from queue import PriorityQueue
input = sys.stdin.readline
pq = PriorityQueue()

n = int(input())
for i in range(n):
    pq.put(int(input()))

result = 0
while True:
    t = pq.get() + pq.get()
    result += t
    if not pq.queue:
        break
    pq.put(t)
print(result)