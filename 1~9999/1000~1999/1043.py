import sys
input = sys.stdin.readline
n,m = map(int,input().split())
tp_list = list(map(int,input().split()))
tp_list.pop(0)

parents = [i for i in range(n+1)]

def find(a):
    if parents[a] != a:
        return find(parents[a])
    else:
        return a

def union(a,b):
    a = find(a)
    b = find(b)
    if a!=b:
        parents[b] =a

def check(a,b):
    a= find(a)
    b= find(b)
    if a == b:
        return True
    else:
        return False

party=[[] for _ in range(m)]
for i in range(m):
    party[i] = list(map(int,input().split()))
    party[i].pop(0)

for i in range(m):
    tmp = party[i][0]
    for j in party[i][1:]:
        union(tmp,j)
count = 0
for i in range(m):
    isPossible=True
    tmp = party[i][0]
    for j in range(len(tp_list)):
        if find(tmp) == find(tp_list[j]):
            isPossible=False
            break
    if isPossible:
        count+=1
print(count)