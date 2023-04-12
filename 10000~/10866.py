class deque():
    def __init__(self):
        self.data=[]
    def push_front(self,x):
        self.data.insert(0,x)
    def push_back(self,x):
        self.data.append(x)
    def pop_front(self):
        try:
            print(self.data.pop(0))
        except:
            print(-1)
    def pop_back(self):
        try:
            print(self.data.pop())
        except:
            print(-1)
    def size(self):
        return print(len(self.data))
    def empty(self):
        if len(self.data) >0:
            print(0)
        else:
            print(1)
    def front(self):
        try:
            print(self.data[0])
        except:
            print(-1)
    def back(self):
        try:
            print(self.data[-1])
        except:
            print(-1)

import sys
input = sys.stdin.readline
n  = int(input())

q = deque()
for _ in range(n):
    act = input()
    if ' ' in act:
        act, num = act.split(' ')
        num = int(num[:-1])
    else:
        act = act[:-1]
    if act == 'push_back':
        q.push_back(num)
    elif act == 'push_front':
        q.push_front(num)
    elif act == 'front':
        q.front()
    elif act == 'back':
        q.back()
    elif act == 'size':
        q.size()
    elif act =='empty':
        q.empty()
    elif act == 'pop_front':
        q.pop_front()
    elif act == 'pop_back':
        q.pop_back()