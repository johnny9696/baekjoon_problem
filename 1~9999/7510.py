import sys
input = sys.stdin.readline

T = int(input())
for i in range(1,T+1):
    length = list(map(int,input().split()))
    length.sort()
    print('Scenario #{}:'.format(i))
    if length[2] ** 2 == length[1]**2 + length[0]**2:
        print('yes')
    else:
        print('no')
    print()