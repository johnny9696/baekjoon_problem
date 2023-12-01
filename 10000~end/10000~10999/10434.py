"""
반복해서 각자리 제곱이 1이 되는 경우 행복한 소수
1. 소수 여부 판단
2. 행복한 소수 여부 판단
test_case
test_num num
"""
import sys
input = sys.stdin.readline

T= int(input())
sosu = [i for i in range(10001)]
sosu[1] = 0
for i in range(2, len(sosu)):
    if sosu[i] !=0 :
        t = sosu[i]*2
        while t <=10000:
            sosu[t] = 0
            t = t+sosu[i]
for _ in range(T):
    t_case, num = map(int,input().split())
    if num not in sosu:
        print(t_case, num,'NO')
    else:
        happy_list=[]
        happy_num = 0
        tmp = num
        while happy_num !=1 and happy_num not in happy_list:
            happy_list.append(happy_num)
            happy_num = 0
            tmp = list(str(tmp))
            for i in tmp:
                happy_num += int(i)*int(i)
            tmp = happy_num
        if happy_num == 1:
            print(t_case, num,'YES')
        else:
            print(t_case,num,'NO')