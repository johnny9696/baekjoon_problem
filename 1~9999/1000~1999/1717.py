import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
n, m = map(int, input().split())
n_list = [i for i in range(n+1)]

def find(a):
    if a != n_list[a]:
        n_list[a] =  find(n_list[a])
        return n_list[a]
    else:
        return a

def union(a,b):
    tmp_a = find(a)
    tmp_b = find(b)
    if tmp_b!= tmp_a:
        n_list[tmp_b] = tmp_a

def check(a,b):
    tmp_a = find(a)
    tmp_b = find(b)
    if tmp_b==tmp_a:
        print('YES')
    else:
        print('NO')

for i in range(m):
    action, a,b = map(int,input().split())
    if action  == 0:
        union(a,b)
    else:
        check(a,b)