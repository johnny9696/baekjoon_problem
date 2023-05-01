import sys
input = sys.stdin.readline
s_num = 0
tf= False
for _ in range(10):
    num = int(input())
    if not tf:
        if s_num + num <=100:
            s_num+=num
        else:
            tmp1 = 100 - s_num
            tmp2 = s_num + num - 100
            if tmp2<=tmp1:
                s_num += num
            tf = True
print(s_num)