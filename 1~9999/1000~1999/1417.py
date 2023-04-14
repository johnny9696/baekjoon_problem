import sys
input = sys.stdin.readline

N = int(input())
dasom = int(input())
"""
max 값 다솜이의 차를 구하고,
max값을 저장해서 기준으로 같으면 빼고 아니면 두는 형태
"""
n_list = [int(input()) for _ in range(N-1)] + [0]

c = 0
while dasom <= max(n_list):
    t_max = max(n_list)
    for i in range(len(n_list)):
        if n_list[i] == t_max:
            dasom +=1
            n_list[i] -=1
            c+=1
            break
print(c)

