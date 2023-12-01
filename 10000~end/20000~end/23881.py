import sys
input = sys.stdin.readline

n,m = map(int,input().split())

n_list = list(map(int,input().split()))

def selected_sort(length,t_num):
    i = length
    cnt = 0
    while True:
        if i == 0:
            return -1,0
        tmp = max(n_list[:i])
        if tmp != n_list[i-1]:
            indx = n_list.index(tmp)
            n_list[indx] = n_list[i-1]
            n_list[i-1] = tmp
            cnt +=1
        if cnt == t_num:
            return n_list[indx], n_list[i-1]
        i = i-1

n1,n2 = selected_sort(n,m)
if n1 != -1:
    print('{} {}'.format(n1,n2))
else:
    print(-1)

