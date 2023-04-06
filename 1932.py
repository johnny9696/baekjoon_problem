import sys
input = sys.stdin.readline

m_depth = int(input())
n_list = [[0 for j in range(i)] for i in range(1,m_depth+1)]
for i in range(0,m_depth) :
    t_list = list(map(int,input().split()))
    if i ==0 :
        n_list[i] = t_list
    else:
        for j in range(len(t_list)):
            if j == 0:
                n_list[i][j] = n_list[i-1][j] + t_list[j]
            elif j == len(t_list) -1:
                n_list[i][j] = n_list[i-1][j-1] + t_list[j]
            else:
                n_list[i][j] = max(n_list[i-1][j] + t_list[j],n_list[i-1][j-1] + t_list[j])
print(max(n_list[-1]))