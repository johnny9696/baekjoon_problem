import sys
input= sys.stdin.readline

def fibo(num):
    zero_one = []
    for depth in range(num+2):
        if depth>=len(zero_one):
            if depth == 0:
                zero_one.append([1,0])
            elif depth ==1 :
                zero_one.append([0,1])
            else:
                zero_one.append([zero_one[depth-2][0]+zero_one[depth-1][0],zero_one[depth-2][1]+zero_one[depth-1][1] ])
    return zero_one[num]

n = int(input())
for i in range(n):
    fi_num = int(input())
    result = fibo(fi_num)
    print(result[0],result[1])
