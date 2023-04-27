import sys
from queue import PriorityQueue
input = sys.stdin.readline
C, N = map(int,input().split())
c_cost= [sys.maxsize] * (C+1)
pq = PriorityQueue()
n_list= [list(map(int,input().split())) for _ in range(N)]
c_cost[0] = 0
for i in range(len(c_cost)):
    if c_cost[i] != sys.maxsize:
        for j in range(len(n_list)):
            cost, cust = n_list[j]
            k = 1
            while i+cust*k <=C+cust:
                if i+cust * k <=C:
                    c_cost[i+cust*k] = min(c_cost[i+cust*k], c_cost[i] + cost * k)
                else:
                    c_cost[C] = min(c_cost[C],c_cost[i+cust*(k-1)]+cost, c_cost[C-1]+cost)
                k+=1
print(c_cost[C])