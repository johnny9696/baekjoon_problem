import sys
input = sys.stdin.readline

test_case = int(input())
for _ in range(test_case):
    N = int(input())
    n_list = list(map(int,input().split()))
    T = int(input())
    t_list = list(map(int,input().split()))
    for data in t_list:
        if data in n_list:
            print(1)
        else:
            print(0)