import sys

input = sys.stdin.readline

T = int(input())

for test_case in range(1,T+1):
    n = int(input())
    n_list = list(map(int,input().split()))
    result = []
    while len(result) != n:
        now = n_list.pop()
        sales = (now // 4) * 3
        indx = n_list.index(sales)
        n_list.remove(sales)
        result.append(sales)
    print('Case #{}:'.format(test_case), end=' ')
    for i in range(n):
        print('{}'.format(result.pop()), end =' ')