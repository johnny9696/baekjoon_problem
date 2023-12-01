import sys
input = sys.stdin.readline

class queue():
    def __init__(self):
        self.data=[]
    def push(self,x):
        self.data.append(x)
    def pop(self):
        try:
            print(self.data.pop(0))
        except:
            print(-1)
    def size(self):
        print(len(self.data))
    def empty(self):
        if len(self.data)!=0:
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

n = int(input())
q = queue()
for i in range(n):
    act = input()
    if ' ' in act:
        act, x = act.split()
    else:
        act,_ = act.split('\n')
    if act == 'push':
        q.push(int(x))
    elif act == 'pop':
        q.pop()
    elif act == 'size':
        q.size()
    elif act == 'empty':
        q.empty()
    elif act == 'front':
        q.front()
    elif act == 'back':
        q.back()