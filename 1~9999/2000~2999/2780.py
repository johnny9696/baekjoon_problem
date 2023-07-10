def n_count(num):
    n_list=[[0 for _ in range(10)] for i in range(num)]
    for i in range(num):
        for j in range(10):
            if i == 0:
                n_list[i][j] = 1
            else:
                if j == 0:
                    n_list[i][j] = (n_list[i-1][7]) % 1234567
                elif j == 1:
                    n_list[i][j] = (n_list[i-1][2] + n_list[i-1][4]) % 1234567
                elif j == 2:
                    n_list[i][j] = (n_list[i-1][1] + n_list[i-1][3] +n_list[i-1][5]) % 1234567
                elif j == 3:
                    n_list[i][j] = (n_list[i-1][2] + n_list[i-1][6]) % 1234567
                elif j == 4:
                    n_list[i][j] = (n_list[i - 1][1] + n_list[i - 1][7] + n_list[i-1][5]) % 1234567
                elif j == 5:
                    n_list[i][j] = (n_list[i - 1][2] + n_list[i - 1][4] + n_list[i-1][6] + n_list[i-1][8]) % 1234567
                elif j == 6:
                    n_list[i][j] = (n_list[i - 1][3] + n_list[i - 1][5] + n_list[i-1][9]) % 1234567
                elif j == 7:
                    n_list[i][j] = (n_list[i - 1][4] + n_list[i - 1][8] + n_list[i - 1][0]) % 1234567
                elif j == 8:
                    n_list[i][j] = (n_list[i - 1][5] + n_list[i - 1][7] + n_list[i - 1][9]) % 1234567
                elif j == 9:
                    n_list[i][j] = (n_list[i - 1][6] + n_list[i - 1][8]) % 1234567
    return sum(n_list[num-1]) % 1234567


import sys
input = sys.stdin.readline

T = int(input())
for i in range(T):
    num = int(input())
    print(n_count(num))