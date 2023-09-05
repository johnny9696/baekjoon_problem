import sys

input = sys.stdin.readline

voul =  ('a','e','i','o','u')

l, c = map(int,input().split())
n_list = list(input().split())
n_list.sort()

pw_list = []
def BFS(sp, torf, pw, depth,ja):
    if depth == l and torf and ja>=2:
        pw_list.append(pw)
        return
    else:
        for i in range(sp+1, c):
            if n_list[i] in voul:
                BFS(i,True, pw + n_list[i], depth + 1,ja)
            else:
                BFS(i, torf, pw+n_list[i],depth +1,ja+1)

for i in range(0,c-l+1):
    if n_list[i] in voul:
        BFS(i, True, n_list[i], 1,0)
    else:
        BFS(i, False, n_list[i], 1,1)

for i in pw_list:
    print(i)