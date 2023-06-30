import sys

input = sys.stdin.readline
"""
적어도 한팀이 소수점 득점 둘다 소수 득점이 아닌 경우
5분 간격 90분 최대 18골 -> 소수 리스트 생성
둘다 골을 못넣을 경우 
A 팀이 골을 넣을 경우
B 팀이 골을 넣을 경우
둘다 골을 넣을 경우
"""
# 두 팀 확률
a_per = float(input())/100.0
b_per = float(input())/100.0

per_list=[(1.0-a_per)*(1.0-b_per), (1.0-a_per)*b_per, (1.0-b_per)*a_per, a_per*b_per]
dp_table = [[[0.0 for k in range(20)] for i in range(20)] for j in range(20)]
dp_table[0][0][0] = 1.0
for i in range(1,19):
    for j in range(0,i+1):
        for k in range(0,i+1):
            if j > 0 and k > 0 :
                dp_table[i][j][k] += dp_table[i-1][j-1][k-1] * per_list[3]
            if j > 0 :
                dp_table[i][j][k] += dp_table[i-1][j-1][k] * per_list[2]
            if k > 0 :
                dp_table[i][j][k] += dp_table[i-1][j][k-1] * per_list[1]
            dp_table[i][j][k] += dp_table[i - 1][j][k] * per_list[0]

ans = 0.0
def prime(num):
    if num==0 or num ==1:
        return False
    for i in range(2,num):
        if num%i == 0 :
            return False
    return True

for j in range(0, 19):
    for k in range(0, 19):
        if prime(j) or prime(k):
            ans += dp_table[18][j][k]
print(ans)