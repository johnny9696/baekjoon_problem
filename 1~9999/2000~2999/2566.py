import sys

input= sys.stdin.readline
m_num = -1
m_p = [0,0]
for i in range(1,10):
    n_list = list(map(int,input().split()))
    tmp_max = max(n_list)
    if tmp_max > m_num:
        m_num = tmp_max
        indx = n_list.index(tmp_max) + 1
        m_p = [i, indx]

print(m_num)
print('{} {}'.format(m_p[0],m_p[1]))