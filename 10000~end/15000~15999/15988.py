import sys

"""
1 : 1
2 : 1+1, 2
3 : 1+1+1, 2+1, 1+2 , 3
"""

T = int(input())
n_count = [0,1,2,4]
for i in range(4, 1000001):
    n_count.append((n_count[i-1]+n_count[i-2]+n_count[i-3])%1000000009)

for _ in range(T):
    ques = int(input())
    print(n_count[ques])
    