import sys
input = sys.stdin.readline

class empty_space():
    def __init__(self):
        self.datalist=[]
    def empty(self):
        self.datalist=[]
    def add(self, x):
        if x not in self.datalist:
            self.datalist.append(x)
    def remove(self,x):
        if x in self.datalist:
            self.datalist.remove(x)
    def check(self,x):
        if x in self.datalist:
            print(1)
        else:
            print(0)
    def toggle(self,x):
        if x in self.datalist:
            self.datalist.remove(x)
        else:
            self.datalist.append(x)
    def all(self):
        self.datalist=[x for x in range(1, 21)]

m = int(input())
wow= empty_space()
for _ in range(m):
    text= input()
    if ' ' in text:
        act, num = text.split(' ')
        num = int(num)
    else:
        act= text[:-1]
    if act == 'add':
        wow.add(num)
    elif act =='remove':
        wow.remove(num)
    elif act =='check':
        wow.check(num)
    elif act == 'toggle':
        wow.toggle(num)
    elif act =='all':
        wow.all()
    elif act =='empty':
        wow.empty()
