import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
n = int(input())
m = int(input())

parent=[i for i in range(n+1)]

def find(a):
    if parent[a] != a:
         return find(parent[a])
    else:
        return a

def union(a,b):
    a = find(a)
    b = find(b)
    if a != b:
        parent[b] = a

def chcek(n_list):
    group = None
    n_list = list(set(n_list))
    for i in n_list:
        if group == None:
            group = find(i)
        else:
            tmp = find(i)
            if group != tmp:
                return False
    return True

for i in range(1,n+1):
    n_list = list(map(int,input().split()))
    for j in range(len(n_list)):
        if n_list[j] == 1:
            union(i,j+1)

n_list = list(map(int,input().split()))
if chcek(n_list):
    print('YES')
else:
    print('NO')