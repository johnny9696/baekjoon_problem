"""
N
K
list
번호 계시된 시점 추천 횟수
"""
import sys
input = sys.stdin.readline

N = int(input())
K = int(input())
n_list = list(map(int,input().split()))
top_n = []
for i in range(len(n_list)):
    iorf = False
    for j in range(len(top_n)):
        if top_n[j][0] == n_list[i]:
            top_n[j][2] +=1
            iorf = True
            break
    if not iorf:
        if len(top_n) < N:
            top_n.append([n_list[i],i,1])
        else:
            m_c = sys.maxsize
            m_t = 0
            m_n = 0
            indx = 0
            for j in range(len(top_n)):
                if m_c> top_n[j][2]:
                    m_n,m_t,m_c = top_n[j]
                    indx = j
                elif m_c == top_n[j][2] and m_t>top_n[j][1]:
                    m_n, m_t, m_c = top_n[j]
                    indx = j
            top_n.pop(indx)
            top_n.append([n_list[i],i,1])
top_n.sort()
for i in top_n:
    print(i[0], end = ' ')