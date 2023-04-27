import sys
input = sys.stdin.readline
for _ in range(3):
    yut = list(map(int,input().split()))
    c = 0
    for i in yut:
        if i == 0:
            c +=1
    if c == 0 :
        print('E')
    elif c == 1:
        print('A')
    elif c == 2:
        print('B')
    elif c == 3:
        print('C')
    else:
        print('D')