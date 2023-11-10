import sys

input = sys.stdin.readline

T = int(input())


for _ in range(T):
    J, N = map(int,input().split())
    box = []
    for _ in range(N):
        r,c = map(int,input().split())
        box.append(r*c)
    box.sort(reverse=True)
    for i in range(len(box)):
        J -= box[i]
        if J <=0:
            print(i+1)
            break