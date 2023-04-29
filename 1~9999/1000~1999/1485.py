import sys
input = sys.stdin.readline
test_case = int(input())

def rec(s_p):
    if abs(s_p[0][0]-s_p[1][0]) + abs(s_p[0][1]-s_p[1][1]) == abs(s_p[1][0]-s_p[3][0]) + abs(s_p[1][1]-s_p[3][1]) and abs(s_p[1][0]-s_p[3][0]) + abs(s_p[1][1]-s_p[3][1]) == abs(s_p[3][0]-s_p[2][0]) + abs(s_p[3][1]-s_p[2][1]) and abs(s_p[3][0]-s_p[2][0]) + abs(s_p[3][1]-s_p[2][1]) == abs(s_p[2][0]-s_p[0][0]) + abs(s_p[2][1]-s_p[0][1]):
        x = (s_p[1][0] - s_p[0][0]) * (s_p[2][0] - s_p[0][0])
        y = (s_p[1][1] - s_p[0][1]) * (s_p[2][1] - s_p[0][1])
        if x + y == 0:
            return 1

    return 0
for _ in range(test_case):
    square = [list(map(int,input().split())) for i in range(4)]
    square.sort()
    print(rec(square))
