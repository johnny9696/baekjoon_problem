import sys

input = sys.stdin.readline
N, M  = map(int,input().split())
n_page = list(set(map(int,input().split())))
TF_list =[False] * (N+1)
for i in n_page:
    if i <=N:
        TF_list[i] = True
n_page = []
for i in range(1,N+1):
    if not TF_list[i]:
        n_page.append(i)
result = 0
b_page = -10
for i in range(0,len(n_page)):
    now = n_page[i]
    if now - b_page <=3 :
        result += (now - b_page) * 2
    else:
        result += 7
    b_page = now
print(result)