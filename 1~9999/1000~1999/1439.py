"""
0인 구역 1인 구역을 나눈다.
그 구역이 적은 쪽을 택함
"""

n_list = list(input())
cnt_zeros = 0
cnt_ones = 0
if n_list[0] == '0':
    before = '1'
else:
    before ='0'
for i in range(len(n_list)):
    if before != n_list[i]:
        before = n_list[i]
        if n_list[i] == '0':
            cnt_zeros += 1
        else:
            cnt_ones +=1
print(min(cnt_ones,cnt_zeros))