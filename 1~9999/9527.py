"""
1자리 1의 갯수
1개
2자리 1의 갯수
11 10 2 + 1
3자리수 1의 갯수
111 110 101 100 4 + 2 + 2
4자리수
1111 1110 1101 1100 1011 1010 1001 1000 8 + 4 + 4 + 4
5자리수
11111 11110 11101 11100 11011 11010 11001 11000
10111 10110 10101 10100 10011 10010 10001 10000
16 + 8 + 8 + 8 + 8
각 자리수는 2^(n-1) + 2^(n-2) * (n-1)

숫자 k까지 1의 수
1. k의 자리수 구하기
2. n-1 자리수 1의 합
3. n자리 부터 K까지 자리 수의 합
"""
one_count = [int(2**(n-1) + 2**(n-2) * (n-1)) for n in range(40)]
print(one_count)

def cal_one(x):
    global one_count
    b_num = []
    i = 0
    while x//2 != 0 or x%2 != 0:
        b_num.insert(0,(x%2))
        x=x//2
        i += 1
    if len(b_num) == 0:
        b_num.append(0)
        i = 1
    result = sum(one_count[:i])
    print(result)
    #for i in range(len(b_num)):

    return result
a,b = map(int,input().split())
print(cal_one(b)-cal_one(a-1))