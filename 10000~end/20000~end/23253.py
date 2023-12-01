import sys
input = sys.stdin.readline

N,M = map(int,input().split())

is_possible = True
for i in range(M):
    size = int(input())
    n_books = list(map(int,input().split()))
    for i in range(1,size):
        if n_books[i-1] < n_books[i]:
            is_possible = False


if is_possible:
    print('Yes')
else:
    print('No')