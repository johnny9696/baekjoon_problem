import sys

input = sys.stdin.readline

N = int(input())

class stack():
    def __init__(self):
        self.data = []

    def data_in(self, num):
        self.data.append(num)

    def push(self):
        if len(self.data) == 0:
            print(-1)
        else:
            print(self.data.pop())

    def length(self):
        print(len(self.data))

    def is_empty(self):
        if len(self.data) == 0:
            print(1)
        else:
            print(0)

    def top(self):
        if len(self.data) == 0:
            print(-1)
        else:
            print(self.data[-1])

ss = stack()

for _ in range(N):
    n_list = list(map(int,input().split()))

    if n_list[0] == 1:
        ss.data_in(n_list[1])
    elif n_list[0] == 2:
        ss.push()
    elif n_list[0] == 3:
        ss.length()
    elif n_list[0] == 4:
        ss.is_empty()
    elif n_list[0] == 5:
        ss.top()