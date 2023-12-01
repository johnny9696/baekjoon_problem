import sys
input=sys.stdin.readline
n= int(input())
n_list = list(map(int,input().split()))
n_sort=sorted(list(set(n_list)))
dic = {n_sort[i] : i for i in range(len(n_sort))}
for i in n_list:
    print(dic[i],end=' ')
